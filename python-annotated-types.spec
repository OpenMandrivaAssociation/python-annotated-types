Name:		python-annotated-types
Version:	0.7.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/annotated-types/annotated_types-%{version}.tar.gz
Summary:	Reusable constraint types to use with typing.Annotated
URL:		https://pypi.org/project/annotated-types/
License:	None
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Reusable constraint types to use with typing.Annotated

%prep
%autosetup -p1 -n annotated_types-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/annotated_types
%{py_sitedir}/annotated_types-*.*-info
