%define		fversion	%(echo %{version} |tr r -)
%define		modulename	Hmisc
Summary:	Harrell Miscellaneous
Name:		R-cran-%{modulename}
Version:	3.13r0
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	5ed3c94c11f67244be99922730495206
URL:		http://socserv.socsci.mcmaster.ca/jfox/
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-Formula
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-Formula
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Hmisc package contains many functions useful for data analysis,
high-level graphics, utility operations, functions for computing
sample size and power, importing datasets, imputing missing values,
advanced table making, variable clustering, character string
manipulation, conversion of S objects to LaTeX code, and recoding
variables.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
