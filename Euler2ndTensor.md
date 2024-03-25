---
layout: page
title: Euler angle for 2nd rank tensor transformation
permalink: /euler2ndtensor/
---


<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


Click this [link](https://docs.google.com/spreadsheets/d/1sGk0MLZbCMCfNXPZ0hJoNsRUQG4K0DlyhorEA1PCNYw/edit?usp=sharing) to use on-line Google spreadsheet.

You can also download the microsoft Excell spreadsheet: [link]({% link /libs/Euler_2ndRankTensorTransform.xlsx %})


<img src='/images/spreadsheet.png' width='700'>

Above is a captured image of the spread sheet.



This sheet allows you to put three Euler angles to obtain transformation matrix.
You can also put 2nd rank tensor (and/or 1st rank tensor, i.e., a vector) in a matrix form and obtain the one after the coordinate transformation is applied.

Namely, you obtain the transformation using the transformation rule for the 2nd rank tensor.
For example, a 2nd rank stress tensor $$\sigma$$ is transformed to a new coordinate system, which results in $$\sigma^\prime$$ by applying the transformation matrix $$R$$ as below:

$$
\sigma^\prime_{ij} = R_{ik} \sigma_{kl} R_{jl} \\
$$

We can obtain the trasnformation $${\bf R}$$ as a function of three Euler angles ($$\phi_1,\Phi,\phi_2$$) - look for more about Euler angles [here]({% link euler.md %}).

Note that in the Excel, the summation is performed using [MMULT function](https://support.office.com/en-us/article/MMULT-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb).
