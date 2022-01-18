# `torch.Tensor 模块`


## `tensor.detach()`

* 返回一个新的 `tensor` ，从当前计算图中分离下来。但是仍指向原变量的存放位置，不同之处只是 `requirse_grad` 为 `false` .得到的这个 `tensor` 永远不需要计算器梯度，不具有 `grad` .

* 即使之后重新将它的 `requires_grad` 置为 `true` ,它也不会具有梯度 `grad` .这样我们就会继续使用这个新的 `tensor` 进行计算，后面当我们进行反向传播时，到该调用 `detach()` 的 `tensor` 就会停止，不能再继续向前进行传播.

* `注意：`使用detach返回的tensor和原始的tensor共同一个内存，即一个修改另一个也会跟着改变。


* `作用：`假如 `A网络` 输出了一个 `Tensor` 类型的变量 `a` , `a` 要作为输入传入到 `B网络` 中，如果我想通过损失函数反向传播修改 `B网络` 的参数，但是不想修改 `A网络` 的参数，这个时候就可以使用 `detcah()` 方法



        # y=A(x), z=B(y) 求B中参数的梯度，不求A中参数的梯度

        y = A(x)
        z = B(y.detach())
        z.backward()


* `案例：x.betach：`

        import torch as t

        ## 生成张量x
        x = t.ones(1, requires_grad=True)
        display(x.requires_grad)                 #True

        ## 生成张量y
        y = t.ones(1, requires_grad=True)
        display(y.requires_grad)                 #True

        ## 分离计算图中的张量x，新生成张量x
        x.betach()
        x.requires_grad                          #False

        y = x*y     	                         #tensor([２.])
        y.requires_grad                          #我还是True
        y.retain_grad()                          #y不是叶子张量，要加上这一行

        z = t.pow(y, 2)                          ## y的二次方


        z.backward()                             #反向传播
        
        y.grad                                   # y 的梯度能被计算出
        x.grad                                   # x 的梯度计算不出，因为betach 之后就没有梯度了，所以反向传播到这也不会再往前计算。

    $z 对 y求导： \frac{\partial z}{\partial y}=2$ 

        y.grad：tensor([2.])
        x.grad：无输出




* `案例：不使用 x.betach：`


        import torch as t
        x = t.ones(1, requires_grad=True)
        display(x.requires_grad)                 #True
        y = t.ones(1, requires_grad=True)
        display(y.requires_grad)                 #True


        # x = x.detach()                         #分离之后
        display(x.requires_grad)   

        y = x*y      	                         #tensor([２.])
        display(y.requires_grad)                 #我还是True
        y.retain_grad()                          #y不是叶子张量，要加上这一行

        z = t.pow(y, 2)
        z.backward()                             #反向传播


        y.grad                                   # tensor([2.])
        x.grad                                   # tensor([2.])





