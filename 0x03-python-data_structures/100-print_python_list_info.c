#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int list_Size = PyList_Size(p);
	int i;
	PyListObject *pyObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_Size);
	printf("[*] Allocated = %li\n", pyObj->allocated);
	for (i = 0; i < list_Size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(pyObj->ob_item[i])->tp_name);
}
