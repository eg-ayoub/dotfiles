source ~/.config/zsh/antigen.zsh

antigen use oh-my-zsh

antigen bundle git
antigen bundle pip
antigen bundle command-not-found

antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting

antigen apply

alias gfpush="ggpush --force"

eval "$(starship init zsh)"

path+=("$HOME/.config/emacs/bin")

export PATH
