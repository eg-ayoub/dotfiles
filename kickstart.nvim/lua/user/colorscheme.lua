local ok, _ = pcall(vim.cmd, 'colorscheme ayu-mirage')
if not ok then
  vim.cmd 'colorscheme default' -- if the above fails, then use default
end
