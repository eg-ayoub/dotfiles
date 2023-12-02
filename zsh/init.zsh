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
eval "$(starship init zsh)"

path+=('/home/ayoub/.local/bin')

export PATH
