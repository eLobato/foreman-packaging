%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name bootstrap-sass

Summary: bootstrap-sass is a Sass-powered version of Bootstrap 3
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.3.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/twbs/bootstrap-sass
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(sass) >= 3.3.4
Requires: %{?scl_prefix}rubygem(autoprefixer-rails) >= 5.2.1

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
bootstrap-sass is a Sass-powered version of Bootstrap, ready to drop right into
your Sass powered applications.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/tasks
%{gem_instdir}/templates
%{gem_instdir}/assets
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/*.json
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/*.md
%{gem_instdir}/Rakefile

%changelog
* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-3
- Replace tfm-rubygem-sass with ror41-rubygem-sass (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Sun Dec 29 2013 Dominic Cleal <dcleal@redhat.com> 3.0.3.0-1
- new package built with tito
