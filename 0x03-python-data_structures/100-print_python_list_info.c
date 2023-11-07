#include <Python.h>
/**
* print_python_list_info - prints some basic info about Python lists.
* @p: pointer
* Return: void
*/
void print_python_list_info(PyObject *p) {
    
    if (PyList_Check(p)) {
        PyListObject *list = (PyListObject *)p;

    
        printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
        printf("[*] Allocated = %ld\n", list->allocated);

        
        for (int i = 0; i < Py_SIZE(list); i++) {
            PyObject *item = PyList_GetItem(p, i);
            printf("Element %d: %s\n", i, item->ob_type->tp_name);
        }
    } else {
        
        fprintf(stderr, "Invalid List Object\n");
    }
}
