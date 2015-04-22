let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <SNR>55_yrrecord =YRRecord3()
map  :CtrlPBuffer
nmap v <Plug>SlimeConfig
nmap  <Plug>SlimeParagraphSend
xmap  <Plug>SlimeRegionSend
nnoremap <silent>  :CtrlP
nnoremap  
nnoremap <NL> <NL>
nnoremap  
nnoremap  
nnoremap <silent>  :YRReplace '1', 'p'
nnoremap <silent>  :YRReplace '-1', 'P'
nnoremap  :call GotoFile("new")
nnoremap f :call GotoFile("new")
vnoremap   zf
nnoremap   za
nmap 0 ^
vmap 0 ^
xnoremap <silent> P :YRPaste 'P', 'v'
nnoremap <silent> P :YRPaste 'P'
xmap S <Plug>VSurround
vmap Si S(i_f)
nmap \\u <Plug>CommentaryUndo:echomsg '\\ is deprecated. Use gc'
nmap \\\ <Plug>CommentaryLine:echomsg '\\ is deprecated. Use gc'
nmap \\ :echomsg '\\ is deprecated. Use gc'<Plug>Commentary
xmap \\ <Plug>Commentary:echomsg '\\ is deprecated. Use gc'
nnoremap \c :call CommentWithHashtags()
map \t\ :tabnext
map \tm :tabmove
map \tc :tabclose
map \to :tabonly
map \tn :tabnew
nnoremap \sv :source $MYVIMRC
nnoremap \ev :vsplit $MYVIMRC
nmap <silent> \rv <Plug>SetTmuxVars
nmap <silent> \rs <Plug>NormalModeSendToTmux
vmap <silent> \rs <Plug>SendSelectionToTmux
map \t :VimuxRunLastCommand
map \nf :NERDTreeFind
map \nb :NERDTreeFromBookmark 
map \nn :NERDTreeToggle
map \j :CtrlP
map \o :BufExplorer
map bd :bdelete
map bN :bprev
map bn :bnext
nmap cs <Plug>Csurround
nmap cgc <Plug>ChangeCommentary
xnoremap <silent> d :YRDeleteRange 'v'
nmap ds <Plug>Dsurround
nmap gx <Plug>NetrwBrowseX
nnoremap <silent> gp :YRPaste 'gp'
nnoremap <silent> gP :YRPaste 'gP'
xmap gS <Plug>VgSurround
nmap gcu <Plug>Commentary<Plug>Commentary
nmap gcc <Plug>CommentaryLine
omap gc <Plug>Commentary
nmap gc <Plug>Commentary
xmap gc <Plug>Commentary
nnoremap gf :call GotoFile("")
nmap j gj
vmap j gj
nmap k gk
vmap k gk
xnoremap <silent> p :YRPaste 'p', 'v'
nnoremap <silent> p :YRPaste 'p'
xnoremap <silent> x :YRDeleteRange 'v'
xnoremap <silent> y :YRYankRange 'v'
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
nnoremap <silent> <SNR>55_yrrecord :call YRRecord3()
nnoremap <silent> <Plug>SurroundRepeat .
nmap <silent> <Plug>CommentaryUndo <Plug>Commentary<Plug>Commentary
imap S <Plug>ISurround
imap s <Plug>Isurround
imap  <Plug>Isurround
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set autoread
set backspace=eol,start,indent
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set hidden
set history=700
set hlsearch
set ignorecase
set incsearch
set isfname=@,48-57,/,.,-,_,+,,,#,$,%,~,=,:
set laststatus=2
set nomodeline
set printoptions=paper:letter
set ruler
set runtimepath=~/.vim_runtime/sources/bufexplorer,~/.vim_runtime/sources/ctrlp.vim,~/.vim_runtime/sources/haskellmode-vim,~/.vim_runtime/sources/jellybeans,~/.vim_runtime/sources/nerdtree,~/.vim_runtime/sources/open_file_under_cursor.vim,~/.vim_runtime/sources/peachpuff,~/.vim_runtime/sources/syntastic,~/.vim_runtime/sources/tlib,~/.vim_runtime/sources/vim-airline,~/.vim_runtime/sources/vim-clojure-static,~/.vim_runtime/sources/vim-commentary,~/.vim_runtime/sources/vim-markdown,~/.vim_runtime/sources/vim-repeat,~/.vim_runtime/sources/vim-slime,~/.vim_runtime/sources/vim-surround,~/.vim_runtime/sources/vimux,~/.vim_runtime/sources/yankring,~/.vim,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim74,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after,~/.vim_runtime,~/.vim_runtime/sources/vim-markdown/after
set shiftwidth=4
set showtabline=2
set smartcase
set smarttab
set statusline=\ %{HasPaste()}%F%m%r%h\ %w\ \ CWD:\ %r%{getcwd()}%h\ \ \ Line:\ %l
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set tabline=%!airline#extensions#tabline#get()
set tabstop=4
set wildignore=*.pyc
set nowritebackup
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Documents/all_notes/school/phil_comp/final_project/programming
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 readme.md
badd +1 schelling/main.py
args readme.md schelling/main.py
edit readme.md
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
vmap <buffer> [] <Plug>(Markdown_MoveToPreviousSiblingHeader)
vmap <buffer> [[ <Plug>(Markdown_MoveToPreviousHeader)
nmap <buffer> [] <Plug>(Markdown_MoveToPreviousSiblingHeader)
nmap <buffer> [[ <Plug>(Markdown_MoveToPreviousHeader)
vmap <buffer> ]c <Plug>(Markdown_MoveToCurHeader)
vmap <buffer> ]u <Plug>(Markdown_MoveToParentHeader)
vmap <buffer> ][ <Plug>(Markdown_MoveToNextSiblingHeader)
vmap <buffer> ]] <Plug>(Markdown_MoveToNextHeader)
nmap <buffer> ]c <Plug>(Markdown_MoveToCurHeader)
nmap <buffer> ]u <Plug>(Markdown_MoveToParentHeader)
nmap <buffer> ][ <Plug>(Markdown_MoveToNextSiblingHeader)
nmap <buffer> ]] <Plug>(Markdown_MoveToNextHeader)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:*,b:+,b:-,b:>
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'mkd'
setlocal filetype=mkd
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=Foldexpr_markdown(v:lnum)
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=syntax
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tqr
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=
setlocal includeexpr=
setlocal indentexpr=GetMkdIndent()
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal nomodeline
setlocal modifiable
setlocal nrformats=octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!airline#statusline(1)
setlocal suffixesadd=
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'mkd'
setlocal syntax=mkd
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 1 - ((0 * winheight(0) + 26) / 52)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
