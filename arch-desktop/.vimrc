call plug#begin('~/.vim/plugged')

" Easily add, modify, and remove surrounding symbols and tags 
" i.e. ", ', [, (, etc
Plug 'tpope/vim-surround'

" Git integration
Plug 'tpope/vim-fugitive'

" Feature for commenting out lines
Plug 'preservim/nerdcommenter'

" Fuzzy Finder
Plug 'kien/ctrlp.vim'

" Autocompletion
Plug 'valloric/youcompleteme'

call plug#end()

" Set theme
if exists('+termguicolors')
    let &t_8f="\<Esc>[38;2;%lu;%lu;%lum"
    let &t_8b="\<Esc>[48;2;%lu;%lu;%lum"
    set termguicolors
endif

set background=dark
colorscheme deep-space

" Disable line wrapping
set nowrap

" Add line Numbers
set number

" Make tabs four spaces
set expandtab
set tabstop=4
set shiftwidth=4

" Sets tabs as two spaces
command TTS2 set expandtab | set tabstop=2 | set shiftwidth=2

" Sets tabs as four spaces
command TTS4 set expandtab | set tabstop=4 | set shiftwidth=4

" Converts two spaces tabs into four space tabs
command Retab4 set ts=2 noet | retab! | set et ts=4 | retab

" Converts four space tabs into two space tabs
command Retab2 set ts=4 noet | retab! | set et ts=2 | retab
