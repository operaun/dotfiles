dotfiles
=================
Dotfiles is a enviornment setter which helps someone like below
+ Who want to quickly establish or rebuild personal settings
+ Who want multiple device enviornment are easily synchronized

Simplet way
-----------------
<pre><code>'./bootstrap.py -y'</code></pre>a
Overview
-----------------
This dot files consists of three stages below

+ Stage 1: Install predefined packages from user_editable.py
+ Stage 2: Install configuration from this dotfiles
+ Stage 3: Install custom files for more convenient enviornment 

You can review what each stage does before applying if you want to

Options
-----------------
- '-y' or '--yes' flag: program proceed without any question as if you type 'yes' for all given selection
- 'user_editable': you can edit for your condition or option control
- If you want to add your configuration file, just add it common_configs
