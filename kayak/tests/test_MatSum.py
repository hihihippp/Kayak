import numpy        as np
import numpy.random as npr

from .  import close_float
from .. import constants
from .. import matrix_ops
from .. import util

def test_scalar_value():
    npr.seed(1)

    for ii in xrange(100):
        npX = npr.randn()
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify that a scalar is reproducted.
        assert close_float(Y.value(True), npX)

def test_scalar_grad():
    npr.seed(2)

    for ii in xrange(100):
        npX = npr.randn()
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify that the gradient is one.
        Y.value(True)
        assert Y.grad(X) == 1.0
        assert util.checkgrad(X, Y) < 1e-6

def test_vector_value_1():
    npr.seed(3)

    for ii in xrange(100):
        npX = npr.randn(10,1)
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify the sum.
        assert close_float(Y.value(True), np.sum(npX))

def test_vector_grad_1():
    npr.seed(4)

    for ii in xrange(100):
        npX = npr.randn(10,1)
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify the gradient.
        Y.value(True)
        assert Y.grad(X).shape == npX.shape
        assert np.all(close_float(Y.grad(X), np.ones(npX.shape)))
        assert util.checkgrad(X, Y) < 1e-6

def test_vector_value_2():
    npr.seed(5)

    for ii in xrange(100):
        npX = npr.randn(1,10)
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify the sum.
        assert close_float(Y.value(True), np.sum(npX))

def test_vector_grad_2():
    npr.seed(6)

    for ii in xrange(100):
        npX = npr.randn(1,10)
        X = constants.Parameter( npX )
        Y = matrix_ops.MatSum(X)

        # Verify the gradient.
        Y.value(True)
        assert Y.grad(X).shape == npX.shape
        assert np.all(close_float(Y.grad(X), np.ones(npX.shape)))
        assert util.checkgrad(X, Y) < 1e-6

def test_matrix_value():
    npr.seed(7)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X)

        # Verify the value.
        assert close_float(Y.value(True), np.sum(npX))

def test_matrix_grad():
    npr.seed(8)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X)

        # Verify the value.
        Y.value(True)
        assert Y.grad(X).shape == npX.shape
        assert np.all(close_float(Y.grad(X), np.ones(npX.shape)))
        assert util.checkgrad(X, Y) < 1e-6

def test_nested_value_1():
    npr.seed(9)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X, axis=0)
        Z   = matrix_ops.MatSum(Y)

        assert np.all(close_float(Y.value(True), np.sum(npX, axis=0)))
        assert close_float(Z.value(True), np.sum(npX))

def test_nested_grad_1():
    npr.seed(10)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X, axis=0)
        Z   = matrix_ops.MatSum(Y)

        assert Z.grad(X).shape == npX.shape
        assert np.all(close_float(Z.grad(X), np.ones(npX.shape)))
        assert util.checkgrad(X, Z) < 1e-6

def test_nested_value_2():
    npr.seed(11)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X, axis=1)
        Z   = matrix_ops.MatSum(Y)

        assert np.all(close_float(Y.value(True).ravel(), np.sum(npX, axis=1)))
        assert close_float(Z.value(True), np.sum(npX))

def test_nested_grad_2():
    npr.seed(12)

    for ii in xrange(100):
        npX = npr.randn(10,20)
        X   = constants.Parameter( npX )
        Y   = matrix_ops.MatSum(X, axis=1)
        Z   = matrix_ops.MatSum(Y)

        assert Z.grad(X).shape == npX.shape
        assert np.all(close_float(Z.grad(X), np.ones(npX.shape)))
        assert util.checkgrad(X, Z) < 1e-6
