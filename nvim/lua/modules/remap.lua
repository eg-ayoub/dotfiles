-- leader is space
vim.g.mapleader = " "

-- file explorer key
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

-- telescope
local ts_builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>pf', ts_builtin.find_files, {})
vim.keymap.set('n', '<C-p>', ts_builtin.git_files, {})
vim.keymap.set('n', '<leader>ps', function()
    ts_builtin.grep_string({ search = vim.fn.input("Grep >") })
end)
vim.keymap.set('n', '<leader>vh', ts_builtin.help_tags, {})

-- undotree
vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)

-- fugitive
vim.keymap.set("n", "<leader>gf", vim.cmd.Git)

-- lsp 0 key maps
local lsp_zero = require('lsp-zero')

lsp_zero.on_attach(function(client, bufnr)
    -- see :help lsp-zero-keybindings
    -- to learn the available actions
    lsp_zero.default_keymaps({ buffer = bufnr })
end)

-- move up and down
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- append line
vim.keymap.set("n", "J", "mzJ`z")

-- half page jumps
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

-- search terms stay in the middle
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- paste - don't replace yanked content
vim.keymap.set("x", "<leader>p", [["_dP]])

-- yank to xclip
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])

-- delete without yanking
vim.keymap.set({ "n", "v" }, "<leader>d", [["_d]])

-- format
vim.keymap.set("n", "<leader>f", vim.lsp.buf.format)

-- quick fix nav
vim.keymap.set("n", "<C-k>", "<cmd>cnext<CR>zz")
vim.keymap.set("n", "<C-j>", "<cmd>cprev<CR>zz")
vim.keymap.set("n", "<leader>k", "<cmd>lnext<CR>zz")
vim.keymap.set("n", "<leader>j", "<cmd>lprev<CR>zz")

-- seek and replace
vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])

-- make exec
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })
