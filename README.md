![GG-Penrose](https://github.com/allexlima/cg-penrose/blob/master/penrose/img/icon.png?raw=true)
### Welcome to [CG-]Penrose
### 2D Graphical Transformations Software

Written in Python 3 and Qt5, this software allows the application of 2D graphical geometric transformations like translation, shearing, scale, rotation and reflection / mirroring in a polygon specified by the user.

It is strongly recommended be using some unix-based OS as [Debian](http://debian.org), [Ubuntu](http://www.ubuntu.com/) or [OSX](http://www.apple.com/in/osx/). We just made

We couldn't test  in Windows OS, only in Arch-linux. If you found some bug, please help us to improve this application opening an [issue](https://github.com/allexlima/cg-penrose/issues) and/or sending a [pull request](https://github.com/allexlima/cg-penrose/pulls). 

Don't forget to give an star to this repo =)

* You can see the [app screenshots here](https://github.com/allexlima/cg-penrose/tree/master/screenshots)

## Setup

Hey! You can explore the `Makefile` tags to fastly execute `penrose` app, if you are using a _Linux-like_ operating system :information_desk_person: 

1. Clone the repo
            
    ```bash
    $ git clone https://github.com/allexlima/PyBestfit.git
    $ cd PyBestfit/
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

---

Developed by [Allex Lima](http://allexlima.com), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python 3.6](https://www.python.org/) and [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download)! 
###### Copyright © 2017 [CG-Penrose](https://github.com/allexlima/cg-penrose) - Licensed by MIT LICENSE.
