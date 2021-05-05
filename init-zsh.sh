# start starship shell prompt
export STARSHIP_CONFIG=~/repos/dotfiles/starship.toml
eval "$(starship init zsh)"

# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi

# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

if [[ -e ~/repos/ohmyzsh/lib/directories.zsh ]]; then
  source ~/repos/ohmyzsh/lib/directories.zsh
fi

if [[ -e ~/repos/ohmyzsh/plugins/git/git.plugin.zsh ]]; then
  if [[ -e ~/repos/ohmyzsh/lib/git.zsh ]]; then
    source ~/repos/ohmyzsh/lib/git.zsh
  fi
  source ~/repos/ohmyzsh/plugins/git/git.plugin.zsh
fi


# change default browser
export BROWSER='/usr/bin/google-chrome-stable'

# vim as manpager
export MANPAGER="env MAN_PN=1 vim -M +MANPAGER -"

# repos
: > ~/.repo_list
find ~/repos -name .git -type d -prune | while read d; do
   cd $d/..
   echo "$PWD" >> ~/.repo_list
   cd $OLDPWD
done


# some other aliases
alias _='sudo'
alias _p='sudo pacman'


alias birth='cd ~/repos/thebirth'
alias xssh='TERM=xterm ssh'
alias hgrep="history 0 | ag"
alias notes="swallow notepadqq ~/notepad.md"
alias evimrc="vim ~/.vimrc"
alias egitconfig="vim .gitconfig"
alias ezshrc="vim ~/.zshrc"
alias ei3rc="vim ~/.i3/config"
alias eicons="vim ~/.i3/app-icons.json"
alias gfpush='git push --force-with-lease --set-upstream origin $(git_current_branch)'
alias _scratch="i3-msg move scratchpad"

~/repos/fm6000 -c yellow -dog
