" VIMRC FOR MY UBUNTU IN WINDOWS
set nocompatible
set number
set mouse =a
set backspace=indent,eol,start 
set shiftwidth =4
set tabstop =4
set softtabstop=4
set expandtab
set clipboard=unnamed
set relativenumber
set noswapfile
set nowrap
set noerrorbells
set laststatus=2
set wrap
set showmode
set smartindent
set autoindent
set incsearch
set hlsearch
set cursorline
syntax on

" installing vim plugin: 
"  git clone https://github.com/VundleVim/Vundle.vim.git && ~/.vim/bundle/Vundle.vim  
" :PluginInstall 
filetype off 
set rtp+=~/.vim/bundle/Vundle.vim
set rtp+=~/.vim/bundle/fzf
set completeopt-=preview
call vundle#begin()
    Plugin 'octol/vim-cpp-enhanced-highlight'
    Plugin 'junegunn/fzf'
call vundle#end()  
filetype plugin indent on 

" syntax highlighting custom colors
" enchaned highlighting needs to be opened
hi Comment ctermfg=238
hi LineNr ctermfg=white
hi PreProc ctermfg=green
hi String ctermfg=107
hi Statement ctermfg=51
hi Type ctermfg=134
hi Function ctermfg=220
hi cCustomClassName ctermfg=203
hi clear CursorLine
hi CursorLine ctermfg=None ctermbg=234

" remembers the last line the cursor was on
if has("autocmd")
      au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal! g`\"zz" | endif
endif
" CUSTOM KEY BINDS
    " PANE MOVEMEN
    nnoremap <silent> <C-s> :vs<CR>:wincmd l<CR>
    nnoremap <silent> <C-d> :sp<CR>:wincmd k<CR>
    nnoremap <silent> <C-j>h :wincmd h<CR>
    nnoremap <silent> <C-j>l :wincmd l<CR>
    nnoremap <silent> <C-j>j :wincmd j<CR>
    nnoremap <silent> <C-j>k :wincmd k<CR>

    " fuzzy finder
    nnoremap <silent> <Tab>f :FZF<CR>

    " writes all the panes
    nnoremap <silent> <C-a> :wa<CR>
    nnoremap <silent> <C-w> :w<CR>
    inoremap <silent> <C-w> <Esc>:w<CR>
    nnoremap <silent> <C-q> :q!<CR>
    nnoremap <silent> <C-e> :wq<CR>
    nnoremap <silent> <C-g> :noh<CR>

    nnoremap <silent> <C-c> <C-q>
    nnoremap <silent> <CR>m :w<CR>:!printf "\e[1;31m\t~~~~~~~~~~~~~new compile~~~~~~~~~~~~~\n\e[0m" && make && ./main<CR>
    nnoremap <silent> <CR>p :w<CR>:!printf "\e[1;31m\t~~~~~~~~~~~~~new compile~~~~~~~~~~~~~\n\e[0m" && python3 %
    nnoremap <CR>1 :!

    " Easier Movement Just replacing tab with shift
    nnoremap <Space>j <c-D>
    nnoremap <Space>k <c-U>

    " Moving between buffers
    " Moving between ctags
    nnoremap <Tab>] <c-]>
    nnoremap <Tab>[ <c-[>

    " Goes to top, bottom of screen
    nnoremap <Space>h <S-h>
    nnoremap <Space>l <S-l>
    nnoremap <Space>f <c-f>
    nnoremap <Space>d <c-b>

    " Moves screen down, up 1
    " Centers cursor middle
    nnoremap <c-m> <c-e>
    nnoremap <c-n> <c-y>
    nnoremap <Space>m <s-M>
    nnoremap <silent> <SPACE><SPACE> zz

    nnoremap n ^
    nnoremap N g_

    " to be able to search for highlighted words
    vnoremap // y/\V<C-R>=escape(@",'/\')<CR><CR>

    " New way to escape 
    inoremap <silent> <c-j> <c-[>
    vnoremap <silent> <c-j> <c-[>

    nnoremap <silent> <c-x> d$

    " To resize window
    nnoremap <silent> <C-j>- :resize -5<CR>
    nnoremap <silent> <C-j>= :resize +5<CR>

    nnoremap <silent> - :vertical resize -5<CR>
    nnoremap <silent> = :vertical resize +5<CR>

" INERT MODE 
let &t_SI = "\e[6 q"
" REPLACE MODE
let &t_SR = "\e[0 q"
" OTHER MODE
let &t_EI = "\e[2 q" 

" text color : rgb(215,175,135)
" background color : rgb(8,8,8)
