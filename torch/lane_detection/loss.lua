
require 'torch'   -- torch
require 'nn'      -- provides all sorts of loss functions

-- 10-class problem
noutputs = 2
----------------------------------------------------------------------
print '==> define loss'

model:add(nn.LogSoftMax())
criterion = nn.ClassNLLCriterion()

-- criterion = nn.MultiMarginCriterion()

----------------------------------------------------------------------
print '==> here is the loss function:'
print(criterion)
