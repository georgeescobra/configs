" VIMRC FOR MY UBUNTU IN WINDOWS
set number
set mouse =a
set backspace=indent,eol,start 
set shiftwidth =4
set tabstop =4
set expandtab
set clipboard=unnamed
set cursorline
set relativenumber
set noswapfile
set nowrap
set incsearch
set noerrorbells
set laststatus=2
set wrap
set noshowmode
syntax on


" installing vim plugin: 
"  git clone https://github.com/VundleVim/Vundle.vim.git && ~/.vim/bundle/Vundle.vim  
" :PluginInstall 
filetype off 
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
    Plugin 'octol/vim-cpp-enhanced-highlight'
call vundle#end()  
filetype plugin indent on 

" syntax highlighting custom colors
hi Comment ctermfg=238
hi LineNr ctermfg=white
hi PreProc ctermfg=blue
hi String ctermfg=107
hi Statement ctermfg=51
hi Type ctermfg=134
hi Function ctermfg=220
hi cCustomClassName ctermfg=203

" CUSTOM KEY BINDS
    " PANE MOVEMENT
    nnoremap <silent> <Tab>s :vs<CR>
    nnoremap <silent> <Tab>d :sp<CR>
    nnoremap <silent> <Tab>h :wincmd h<CR>
    nnoremap <silent> <Tab>l :wincmd l<CR>
    nnoremap <silent> <Tab>j :wincmd j<CR>
    nnoremap <silent> <Tab>k :wincmd k<CR>
    " writes all the panes
    nnoremap <silent> <Tab>wa :wa<CR>
    nnoremap <silent> <Tab>w :w<CR>
    nnoremap <silent> <Tab>q :q<CR>
    " This is to go to last line you working on
    nnoremap <silent> <Space>t `" 
    nnoremap <silent> <Tab>m :!make
    nnoremap <Tab>1 :!

    nnoremap <Tab>e :edit 

    " Easier Movement Just replacing tab with shift
    nnoremap <Space>j <c-D>
    nnoremap <Space>k <c-U>

    " Goes to top, bottom of screen
    nnoremap <Space>h <S-h>
    nnoremap <Space>l <S-l>

    " Moves screen down, up 1
    " Centers cursor middle
    nnoremap <Space>n <c-e>
    nnoremap <Space>b <c-y>
    nnoremap <Space>m <s-M>


    nnoremap n ^
    nnoremap <S-n> g_

" INERT MODE 
let &t_SI = "\e[6 q"
" REPLACE MODE
let &t_SR = "\e[0 q"
" OTHER MODE
let &t_EI = "\e[2 q" 

" text color : rgb(215,175,135)
" background color : rgb(8,8,8)
