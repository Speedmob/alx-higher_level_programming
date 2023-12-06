#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - prints Bytes object
 * @p: PyObject
*/
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}
/**
 * print_python_list - prints list info of a PyObject
 * @p: PyObject
*/
void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int i;
        PyListObject *Pylist = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", Pylist->allocated);
        for (i = 0; i < size; i++)
        {
                type = (Pylist->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(Pylist->ob_item[i]);
        }
}
