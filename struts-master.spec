Name:          struts-master
Version:       8
Release:       1
Summary:       Master pom file for Apache struts projects
Group:         Development/Java
License:       ASL 2.0
URL:           https://struts.apache.org/
# http://svn.apache.org/repos/asf/struts/maven/tags/STRUTS_MASTER_8/pom.xml
Source0:       struts-master-pom.xml

BuildRequires: jpackage-utils

Requires:      maven-release-plugin

Requires:      jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:      java
BuildArch:     noarch

%description
The goal of the Apache Struts project is to encourage application 
architectures based on the "Model 2" approach, a variation of the classic 
Model-View-Controller (MVC) design paradigm. Under Model 2, a servlet (or 
equivalent) manages business logic execution, and presentation logic 
resides mainly in server pages.

This package contains the master pom file for the apache struts project.

%prep

%build

%install

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE0} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

