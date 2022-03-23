import sys
import cv2
import copy
import numpy as np
import torch
import torch.backends.cudnn as cudnn

sys.path.append("./yolov5")

from ui.style import *
from ui.ui import *

from qt_material import apply_stylesheet
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from yolov5.utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr,
                                  increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer,
                                  xyxy2xywh)
from yolov5.utils.plots import Annotator, colors, save_one_box
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.augmentations import letterbox
from filter.filter import *

theme = './ui/my_theme'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.im0 = None
        self.imc = None
        self.centers = []
        self.timer_video = QTimer()
        self.yamlFileType = None
        self.ptFileType = None
        self.lastPtFile = "best.pt"
        self.ptFileName = self.lastPtFile
        self.lastYamlFile = "data/blastHole.yaml"
        self.yamlFileName = self.lastYamlFile
        self.started = False
        self.setupUi(self)
        # self.ui = Ui_MainWindow()
        # self.setupUi(self)
        self.parse = {
            "source": "--source 1",
            "imgsz": "--imgsz 1280",
            "weights": "--weights yolov5/best.pt",
            "data": "--data yolov5/data/blastHole.yaml",
            "filter": "--filter",
            "show_conf": "",
            "conf": "--conf-thres 0.25",
            "iou": "--iou-thres 0.45"
        }
        self.opt = {}
        self.init_slots()
        self.save_fig()
        self.ViewSize = self.CV.geometry().getRect()[2:]
        self.cap = cv2.VideoCapture()
        self.device = select_device("")
        self.half = False

        cudnn.benchmark = True

    def init_slots(self):
        self.timer_video.timeout.connect(self.show_frame)
        self.confSlider.valueChanged.connect(self.threshold_changed)
        self.IoUSlider.valueChanged.connect(self.threshold_changed)
        self.buttonCamera.clicked.connect(self.camera_on)
        self.buttonCapture.clicked.connect(self.capture_on)
        self.buttonProcess.clicked.connect(self.process_on)
        self.modelChoose.clicked.connect(self.choose_model)
        self.yamlChoose.clicked.connect(self.choose_yaml)
        self.imgSize.stateChanged.connect(self.image_size)
        self.sourceChoose.clicked.connect(self.choose_source)
        self.noConf.stateChanged.connect(self.toggle_settings)
        self.filter.stateChanged.connect(self.toggle_settings)
        self.editSource.textChanged.connect(self.change_source)
        self.editSize.textChanged.connect(self.change_imgsz)
        self.buttonStop.clicked.connect(self.stop)
        self.buttonStart.clicked.connect(self.start)

    def start(self):
        if not self.started:
            self.started = True
            if self.buttonCamera.isChecked():
                # source = self.parse["source"].split(" ")[-1]
                source = eval(self.opt["source"]) if self.opt["source"].isnumeric() else self.opt["source"]
                flag = self.cap.open(source, cv2.CAP_DSHOW)
                if not flag:
                    QMessageBox.warning(
                        self, u"Warning", u"打开摄像头失败", buttons=QMessageBox.Ok,
                        defaultButton=QMessageBox.Ok)
                else:
                    # self.cap.release()/ self.ViewSize[1] > 16 / 9
                    # self.ViewSize = self.CV.geometry().getRect()[2:]
                    # print("ViewSize:", self.ViewSize)
                    # h_min = min(self.ViewSize[0] / 16 * 9, self.ViewSize[1])
                    # self.ViewSize = [int(h_min / 9 * 16), int(h_min)]
                    # print("Resize:", self.ViewSize)
                    self.timer_video.start(30)

            if not self.buttonCamera.isChecked() and \
                    not self.buttonCapture.isChecked() and \
                    not self.buttonProcess.isChecked():
                self.started = False
                print("Loading Model With Opts...")
                self.model = DetectMultiBackend(weights=self.opt["weights"],
                                                device=self.device,
                                                dnn=False,
                                                data=self.opt["data"])
                self.stride, \
                self.names, \
                self.pt, \
                self.jit, \
                self.onnx, \
                self.engine = \
                    self.model.stride, \
                    self.model.names, \
                    self.model.pt, \
                    self.model.jit, \
                    self.model.onnx, \
                    self.model.engine

                print("Image Size:", self.opt["imgsz"], type(self.opt["imgsz"]))
                self.imgsz = (check_img_size(self.opt["imgsz"], s=self.stride),) * 2
                print("Image Size:", self.imgsz, type(self.imgsz))
                self.half &= (self.pt or self.jit or self.onnx or self.engine) and self.device.type != 'cpu'
                if self.pt or self.jit:
                    self.model.half() if self.half else self.model.model.float()
                elif self.engine and self.model.trt_fp16_input != self.half:
                    print('model ' + (
                        'requires' if self.model.trt_fp16_input else 'inco with') + '--half. Adjusting automatically')
                    self.half = self.model.trt_fp16_input
                self.model.warmup(imgsz=(1, 3, *self.imgsz), half=self.half)
                print("Model Loaded Successfully! Half:", self.half)

    @torch.no_grad()
    def predict(self, img):
        # Padded resized
        img = letterbox(img, new_shape=self.imgsz, stride=self.stride, auto=True)[0]
        # HWC 2 CHW, BGR 2 RGB
        img = img.transpose((2, 0, 1))[::-1]
        # 将mat连续存储，加速访问和修改
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()
        # 归一化处理 0~255 -> 0.0~1.0
        img /= 255.0
        # expand for batch dim
        if len(img.shape) == 3:
            img = img[None]

        pred = self.model(img, augment=False, visualize=False, val=False)
        pred = non_max_suppression(pred, self.opt["conf"], self.opt["iou"], None, False, max_det=500)

        return img, pred

    def show_frame(self):
        flag, img = self.cap.read()
        if self.filter.isChecked():
            img = cv2.filter2D(img, -1, kernel_outline)
        if img is not None:
            # 记录原尺寸
            imageSourceShape = img.shape
            # 保留原图形备份
            self.imc = copy.deepcopy(img)
            self.im0 = copy.deepcopy(img)
            img, pred = self.predict(img)
            annotator = Annotator(self.imc, line_width=3, example=str(self.names))
            for i, det in enumerate(pred):
                if len(det):
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], imageSourceShape).round()

                    self.centers = []
                    for *xyxy, conf, cls in reversed(det):
                        cx = int((xyxy[0] + xyxy[2]) / 2)
                        cy = int((xyxy[1] + xyxy[3]) / 2)
                        self.centers.append((cx, cy))
                        label = self.names[int(cls)] if self.opt["hide_conf"] else f"{self.names[int(cls)]} {conf:.2f}"
                        annotator.box_label(xyxy, label, color=colors(int(cls) + 3, True))

                    self.centers.sort()

            self.result = self.imc
            # print(self.centers)
            showImage = QImage(self.result.data,
                               self.result.shape[1],
                               self.result.shape[0],
                               QImage.Format_BGR888)
            self.CV.setPixmap(QPixmap.fromImage(showImage))


        else:
            self.timer_video.stop()
            self.cap.release()
            self.CV.clear()
            self.stop()

    def stop(self):
        if self.started:
            self.cap.release()
            self.started = False
            self.timer_video.stop()

        self.buttonCamera.setChecked(False)
        self.buttonCapture.setChecked(False)
        self.buttonProcess.setChecked(False)
        print()

    def threshold_changed(self):
        self.valThreshold.setText(str(self.confSlider.value()) + "%")
        self.valIOUThreshold.setText(str(self.IoUSlider.value()) + "%")
        self.parse["conf"] = "--conf-thres " + str(self.confSlider.value() / 100)
        self.parse["iuo"] = "--iou-thres " + str(self.IoUSlider.value() / 100)
        self.save_fig()

    def camera_on(self):
        if not self.buttonCamera.isChecked():
            self.buttonCamera.setChecked(True)
        self.buttonCapture.setChecked(False)
        self.buttonProcess.setChecked(False)
        self.capture_off()
        self.porcess_off()

    def camera_off(self):
        pass

    def capture_on(self):
        self.stop()
        if not self.buttonCapture.isChecked():
            self.buttonCapture.setChecked(True)
        self.buttonCamera.setChecked(False)
        self.buttonProcess.setChecked(False)
        self.camera_off()
        self.porcess_off()

    def capture_off(self):
        pass

    def process_on(self):
        self.stop()
        if not self.buttonProcess.isChecked():
            self.buttonProcess.setChecked(True)
        self.buttonCamera.setChecked(False)
        self.buttonCapture.setChecked(False)
        self.camera_off()
        self.capture_off()
        self.imc = copy.deepcopy(self.im0)
        img = self.imc
        if img is not None:
            # 记录原尺寸
            imageSourceShape = img.shape
            img, pred = self.predict(img)
            annotator = Annotator(self.imc, line_width=3, example=str(self.names))
            for i, det in enumerate(pred):
                if len(det):
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], imageSourceShape).round()

                    self.centers = []
                    for *xyxy, conf, cls in reversed(det):
                        cx = int((xyxy[0] + xyxy[2]) / 2)
                        cy = int((xyxy[1] + xyxy[3]) / 2)
                        self.centers.append((cx, cy))
                        label = self.names[int(cls)] if self.opt["hide_conf"] else f"{self.names[int(cls)]} {conf:.2f}"
                        annotator.box_label(xyxy, label, color=colors(int(cls) + 3, True))

                    # Add By XiaMoo
                    self.centers.sort()
                    for j in range(len(self.centers) - 1 if len(self.centers) > 0 else 0):
                        cv2.circle(self.imc, self.centers[j], 7, (255, 255, 255), -1)
                        cv2.line(self.imc, self.centers[j], self.centers[j + 1], (255, 255, 0), 3)
                    if len(self.centers):
                        cv2.circle(self.imc, self.centers[-1], 7, (255, 255, 255), -1)

            self.result = self.imc
            print(self.centers)
            showImage = QImage(self.result.data,
                               self.result.shape[1],
                               self.result.shape[0],
                               QImage.Format_BGR888)
            self.CV.setPixmap(QPixmap.fromImage(showImage))

    def porcess_off(self):
        pass

    def choose_source(self):
        if self.sourceChoose.isChecked():
            self.editSource.setReadOnly(False)
        else:
            self.editSource.setText("0")
            self.editSource.setReadOnly(True)
        self.change_source()

    def choose_model(self):
        self.ptFileName, self.ptFileType = QFileDialog.getOpenFileName(self,
                                                                       "选择文件",
                                                                       "../",
                                                                       "(*.pt)")
        if not self.ptFileName:
            self.modelLabel.setText(self.lastPtFile.split("/")[-1])
            self.parse["weights"] = "--weights " + self.lastPtFile
            print("Model Chosen:", self.lastPtFile)
        else:
            self.modelLabel.setText(self.ptFileName.split("/")[-1])
            self.parse["weights"] = "--weights " + self.ptFileName
            self.lastPtFile = self.ptFileName
            print("Model Chosen:", self.ptFileName)
        self.save_fig()

    def choose_yaml(self):
        self.yamlFileName, self.yamlFileType = QFileDialog.getOpenFileName(self,
                                                                           "选择文件",
                                                                           "../",
                                                                           "(*.yaml)")
        if not self.yamlFileName:
            self.Yaml.setText(self.lastYamlFile.split("/")[-1])
            self.parse["data"] = "--data " + self.lastYamlFile
            print("Model Chosen:", self.lastYamlFile)
        else:
            self.Yaml.setText(self.yamlFileName.split("/")[-1])
            self.parse["data"] = "--data " + self.yamlFileName
            self.lastYamlFile = self.yamlFileName
            print("Model Chosen:", self.yamlFileName)
        self.save_fig()

    def image_size(self):
        if self.imgSize.isChecked():
            self.editSize.setReadOnly(False)
            # self.editSize.setText("1280")
        else:
            self.editSize.setReadOnly(True)
            self.editSize.setText("1280")
            # self.parse["imgsz"] = "--img-size 1280"
        self.change_imgsz()

    def toggle_settings(self):
        if self.noConf.isChecked():
            self.parse["show_conf"] = "--hide-conf"
        else:
            self.parse["show_conf"] = ""
        if self.filter.isChecked():
            self.parse["filter"] = "--filter"
        else:
            self.parse["filter"] = ""
        self.save_fig()

    def change_source(self):
        if src := self.editSource.text():
            self.parse["source"] = "--source " + src
        else:
            self.parse["source"] = ""
        self.save_fig()

    def change_imgsz(self):
        self.parse["imgsz"] = "--imgsz " + self.editSize.text()
        self.save_fig()

    def save_fig(self):
        # parse_str = ""
        # for param in self.parse:
        #     parse_str += "%s"%self.parse[param]
        parse_str = " ".join(self.parse.values())
        self.params.setText(parse_str)
        self.opt["source"] = self.parse["source"].split(" ")[-1]
        self.opt["imgsz"] = eval(self.parse["imgsz"].split(" ")[-1])
        self.opt["weights"] = self.parse["weights"].split(" ")[-1]
        self.opt["data"] = self.parse["data"].split(" ")[-1]
        self.opt["filter"] = self.filter.isChecked()
        self.opt["hide_conf"] = self.noConf.isChecked()
        self.opt["conf"] = self.confSlider.value() / 100
        self.opt["iou"] = self.IoUSlider.value() / 100
        print("Opt Changed:")
        for arg in self.opt:
            print(arg, self.opt[arg], type(self.opt[arg]), sep="\t")
        print()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme + '.xml',
                     invert_secondary=(
                             'light' in theme and 'dark' not in theme),
                     extra=extra)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
