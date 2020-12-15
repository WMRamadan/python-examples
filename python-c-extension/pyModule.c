#include <Python.h>

int Cfib(int n)
{
    if (n < 2)
        return n;
    else
        return Cfib(n-1)+Cfib(n-2);
}

static PyObject* fib(PyObject* self, PyObject* args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    
    return Py_BuildValue("i", Cfib(n));
}

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s", "Version 1.0");
}

static PyMethodDef pyMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculate the fibonacci numbers."},
    {"version", (PyCFunction)version, METH_NOARGS, "Returns the version."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyModule = {
    PyModuleDef_HEAD_INIT,
    "pyModule",
    "Fibonacci Module",
    -1,
    pyMethods
};

PyMODINIT_FUNC PyInit_pyModule(void)
{
    return PyModule_Create(&pyModule);
}