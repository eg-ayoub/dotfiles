call plug#begin('~/.config/vim/plugged')

Plug 'tpope/vim-sensible'
Plug 'itchyny/lightline.vim'
Plug 'junegunn/seoul256.vim'
Plug 'preservim/nerdtree'
Plug 'ycm-core/YouCompleteMe'
Plug 'preservim/nerdcommenter'
Plug 'kien/ctrlp.vim'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-fugitive'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'jiangmiao/auto-pairs'
Plug 'OmniSharp/omnisharp-vim'
Plug 'kien/rainbow_parentheses.vim'
" Plug 'mg979/vim-visual-multi'
Plug 'ekalinin/Dockerfile.vim'

call plug#end()

" lightline config
let g:lightline = {
	\ 'colorscheme': 'seoul256',
	\}
let g:lightline = {
      \ 'colorscheme': 'seoul256',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'FugitiveHead'
      \ },
      \ }

" color mapping 
let g:seoul256_background = 233
colo seoul256
set background=dark

" change leader
let mapleader=" "

" some bindings

" window manipulation  bindings
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" NERDTree bindings
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

" YCM bindings
nnoremap <leader>gd :YcmCompleter GoTo<CR>

" CTRLP bindings
nnoremap <leader>p :CtrlP<CR>

" Go to tab by number
noremap <leader>1 1gt
noremap <leader>2 2gt
noremap <leader>3 3gt
noremap <leader>4 4gt
noremap <leader>5 5gt
noremap <leader>6 6gt
noremap <leader>7 7gt
noremap <leader>8 8gt
noremap <leader>9 9gt
noremap <leader>0 :tablast<cr>

" use ag
if executable('ag')
	" use ag over grep
	set grepprg=ag\ --nogroup\ --nocolor\ --column
	
	" use ag in ctrlp
	let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'
	
	" no need for cache anymore
	let g:ctrlp_use_caching = 0
endif

" some salt-vim necessary stuff
syntax on
set nocompatible
filetype plugin indent on

" line numbers
:set number
:set noshowmode

" Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif

" odd extensions
autocmd BufNewFile,BufRead *.sls set syntax=yaml
autocmd BufNewFile,BufRead *.yml.j2 set syntax=jinja

" rainbow parentheses stuff
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces

" default to 4spaces per tab
:set tabstop=4

" cursor line 
:set cursorline

" tabs view
:set listchars=tab:\┊\ 
:set list
