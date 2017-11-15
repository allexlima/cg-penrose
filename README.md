<img src="https://github.com/allexlima/cg-penrose/blob/master/penrose/img/icon.png?raw=true" width="64">

## Welcome to CG-Penrose v1.2b

[![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

CG-Penrose is a software developed using Python 3.6 and Qt5, in Computer Graphics discipline, taught by prof. Jonatas Oliveira. It can help you to simulate lines rasterization and calculate 2D transformations on polygons.

**Features:**
 - 2D Geometric transformations like translation, **shearing**, **scaling**, **rotation** and **reflection/mirroring** in any polygon specified by you.
 - Simulate line rasterization using algorithms like **Digital Differential Analyzer (DDA)** and **Bresenham Line-Drawing**


:star2: Don't forget to give an star to this repo =)

#### Index

1. [Setup](https://github.com/allexlima/cg-penrose#setup) 
3. [Basic usage](https://github.com/allexlima/cg-penrose#basic-usage)

## Setup

* Using `Makefile`:

    *Supported only in linux-like operating systems yet* :information_desk_person:
    
    Prepare everything using only
    
    ```bash
    $ make
    ```
    
    Then,
    
    ```bash
    $ make run
    ```
    
    and be happy :)

\~**OR**\~

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

## Basic Usage

**How use line rasterization functions?**

- Insert, using the **push** button exactly 2 vertices. Then, navigate to **Tools > Rasterize line with...** and choose any algorithm.

**How to apply one or more transformations in a 2D polygon?**

- First, you should know that you must insert at least 3 vertices through the **'push' button**, in the main screen. After this, you can render your polygon clicking in **Tools > Render**, or pressing **F4 key** shortcut. 

- With you polygon rendered, now you can apply any of one transformations available in the **2D Transformations** tab. You can check the selected transformation an set the necessary parameters, then you should click in **Tools > Update** or press **F5 key** to apply and see the output.  



---

Developed by [Allex Lima](http://allexlima.com), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python 3.6](https://www.python.org/) and [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download)! 
###### Copyright © 2017 [CG-Penrose](https://github.com/allexlima/cg-penrose) - Licensed by MIT LICENSE.
