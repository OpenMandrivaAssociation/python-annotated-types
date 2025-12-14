Name:		python-annotated-types
Version:	0.7.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/a/annotated-types/annotated_types-%{version}.tar.gz
Summary:	Reusable constraint types to use with typing.Annotated
URL:		https://pypi.org/project/annotated-types/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildArch:	noarch

%description
Reusable constraint types to use with typing.Annotated

%files
%{py_sitedir}/annotated_types
%{py_sitedir}/annotated_types-*.*-info
