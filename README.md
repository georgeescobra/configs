## MY CONFIG FILES
    THIS IS TO STORE ALL MY CONFIGS THAT I USE
    use setup.py to handle and keep track of all configs
    needs python3 > 3.8
    These configs are bash specific
    '.txt' file extension is used to differentiate a config template to other files
    TO RUN: $chmod +x setup.py
            $./setup.py --<flag>
#### FLAGS:
    --install:
        This is good to set up the configs.
        Copies the configs from the repo into ~ <home directory>
        Sets up a cache to store the previous versions in case the newer one fails
    --update:
        This is good to keep track and update the config if it was changed locally
        Copies the configs from the ~ <home directory> to the configs repo
    --reset:
        This resets all of the config files from cache
    setup.py contains all configuration defaults at the top of the file

### TODO:
    * will do this at some point *
    - differentiate between different shells and operating systems
        - just add <shellType | osType>.<config>.txt
    - Also look at vimrc and run necessary commands for vundle (probably should also write a function for this)
    - brew install coreutils -> for MACOS using dircolors


