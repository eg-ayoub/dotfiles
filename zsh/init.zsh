source ~/.config/zsh/antigen.zsh

antigen use oh-my-zsh

antigen bundle git
antigen bundle pip
antigen bundle command-not-found

antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting

antigen apply

alias gfpush="ggpush --force"
alias lssh="TERM=xterm ssh -F ssh_config"
alias lscp="scp -F ssh_config"
alias nv="nvim ."
eval "$(starship init zsh)"

function spl () { for x in {1..$1}; do alacritty & sleep 0.2 && disown ; done  }

function fail () { echo $1 && return 1 }

function worktree () {
    setopt local_options err_return
    git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "Not in a git directory"
    [[ -z $1 ]] && fail "Please specify worktree name"
    reponame="$(basename $(git remote get-url origin))"
    [[ -z "$reponame" ]] && fail "failed to fetch repository name"
    treeloc="$HOME/repos/worktrees/$reponame/$1"
    git worktree add -B "$1" "$treeloc" "$(git_current_branch)"
    cd $treeloc
}

path+=('/home/ayoub/.local/bin')

export PATH
