<img src="https://github.com/allexlima/cg-penrose/blob/master/penrose/img/icon.png?raw=true" width="64">

## Welcome to CG-Penrose

[![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

### 2D Graphical Transformations Software

Written in Python 3 and Qt5, this software allows the application of 2D graphical geometric transformations like translation, shearing, scale, rotation and reflection/mirroring in a polygon specified by the user.

It is strongly recommended be using some unix-based OS as [Debian](http://debian.org), [Ubuntu](http://www.ubuntu.com/) or [OSX](http://www.apple.com/in/osx/). We couldn't test  in Windows OS, only in some Linux-like distros**. If you found some bug, please help us to improve this application opening an [issue](https://github.com/allexlima/cg-penrose/issues) and/or sending a [pull request](https://github.com/allexlima/cg-penrose/pulls). 

:star2: Don't forget to give an star to this repo =)

#### Index

1. [Setup](https://github.com/allexlima/cg-penrose#setup) 
2. [Screenshots](https://github.com/allexlima/cg-penrose#screenshots)
3. [Basic usage](https://github.com/allexlima/cg-penrose#basic-usage)

## Setup

Hey! You can explore the `Makefile` tags to fastly execute `penrose` app, if you are using a _Linux-like_ operating system :information_desk_person: 

1. Clone the repo
            
    ```bash
    $ git clone https://github.com/allexlima/cg-penrose.git
    $ cd cg-penrose/
    ```

2. Create virtualenv and install the requirements

    ```bash
    $ virtualenv -p python3 env  
    $ source env/bin/activate
    ```
    ```bash

    $ pip install -r requirements.txt
    ```

3. Compile the UIs

    ```bash
    $ python setup.py build_ui
    ```
    
4. Install the package

    ```bash
    $ pip install -e .
    ```
    
5. And finally run `penrose` =)

    ```bash
    $ python -m penrose
    ```

## Screenshots

![](https://github.com/allexlima/cg-penrose/blob/master/screenshots/0.png?raw=true)

![](https://github.com/allexlima/cg-penrose/blob/master/screenshots/1.png?raw=true)

![](https://github.com/allexlima/cg-penrose/blob/master/screenshots/2.png?raw=true)

![](https://github.com/allexlima/cg-penrose/blob/master/screenshots/3.png?raw=true)

![](https://github.com/allexlima/cg-penrose/blob/master/screenshots/4.png?raw=true)

## Basic Usage

**How to apply one or more transformations in a 2D polygon?**

- First, you should know that you must insert at least 3 vertices through the **'push' button**, in the main screen. After this, you can render your polygon clicking in **Tools > Render**, or pressing **F4 key** shortcut. 

- With you polygon rendered, now you can apply any of one transformations available in the **2D Transformations** tab. You can check the selected transformation an set the necessary parameters, then you should click in **Tools > Update** or press **F5 key** to apply and see the output.  



---

Developed by [Allex Lima](http://allexlima.com), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python 3.6](https://www.python.org/) and [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download)! 
###### Copyright © 2017 [CG-Penrose](https://github.com/allexlima/cg-penrose) - Licensed by MIT LICENSE.
