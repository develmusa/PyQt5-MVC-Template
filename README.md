# PyQt5-MVC-Template

:warning: Template is Outdated and needs rework

## Usage
1. Install Dependencies: ```pip3 install -r requirements.txt```
2. Start App: ```python3 src/mvc_app.py```

## Development

### Dev Requirements

- Install `QT-Creator`
  1. Download [QT-Creator](https://www.qt.io/product/development-tools) installer.
  2. Select `QT *.* for desktop development` in the installer.

### Various Infos

- Style Guide: [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Architecture: [Model-View-programming](https://doc.qt.io/qt-5/model-view-programming.html)

### Change to GUI

QTCreator is used to create the visual representation of the GUI (view component). With the QTCreator, the GUI can be created with a graphical interface, and then the corresponding python code can be generated. The generated code must not be modified by hand to make GUI layout adjustments, otherwise the QTCreator and the generated files are no longer coherent.

The QTCreator files to create the views can be found in the [./src/views](./src/views) folder.

#### Workflow

1. Edit `.ui` files in QT-Creator
2. Convert `.ui` files to `.py` for [PyQt5](https://pypi.org/project/PyQt5/) with [pyuic5](https://pypi.org/project/pyuic5-tool/)

    ```bash
    pyuic5 .\src\views\mainView.ui -o .\src\views\main_view_ui.p
    ```
