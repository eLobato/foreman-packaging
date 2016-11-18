%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name select2-rails

Summary: Integrate Select2 javascript library with Rails asset pipeline
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 3.5.10
Release: 2%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/argerim/select2-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygem(thor) >= 0.14
Requires: %{?scl_prefix_ruby}rubygem(thor) < 1
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Select2 is a jQuery based replacement for select boxes. It supports
searching, remote data sets, and infinite scrolling of results. This gem
integrates Select2 with Rails asset pipeline for ease of use.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 3.5.10-2
- Use gem_install macro (dominic@cleal.org)

* Thu Mar 10 2016 Dominic Cleal <dominic@cleal.org> 3.5.10-1
- Update select2-rails to 3.5.10 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.5.9.3-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.5.9.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jun 23 2015 Dominic Cleal <dcleal@redhat.com> 3.5.9.3-1
- new package built with tito