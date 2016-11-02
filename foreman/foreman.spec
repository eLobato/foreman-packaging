%global homedir %{_datadir}/%{name}
%global confdir extras/packaging/rpm/sources
%global foreman_rake %{_sbindir}/%{name}-rake

# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}
%global scl_ruby_bin /usr/bin/%{?scl:%{scl_prefix}}ruby
%global scl_rake /usr/bin/%{?scl:%{scl_prefix}}rake

# set and uncomment all three to set alpha tag
#global alphatag RC1
#global dotalphatag .%{alphatag}
#global dashalphatag -%{alphatag}

Name:   foreman
Version: 1.14.0
Release: 0.develop%{?dotalphatag}%{?dist}
Summary:Systems Management web application

Group:  Applications/System
License: GPLv3+ with exceptions
URL: http://theforeman.org
Source0: http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2
Source1: %{name}.init
Source2: %{name}.sysconfig
Source3: %{name}.logrotate
Source4: %{name}.cron.d
Source5: %{name}.tmpfiles
Source6: %{name}.repo
Source7: %{name}-plugins.repo
Source8: %{name}.gpg
BuildArch:  noarch

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3
Requires: %{?scl_prefix_ruby}rubygem(rdoc)
Requires: %{?scl_prefix}rubygem(bundler_ext)
%if 0%{?scl:1}
Requires: %{scl}-runtime >= 3
Requires: %{scl}-runtime < 4
%endif

Requires: wget
Requires: /etc/cron.d
Requires(pre):  shadow-utils
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts

# Subpackages
Requires: %{name}-debug

# Gemfile
Requires: %{?scl_prefix_ror}rubygem(rails) >= 4.2.5.1
Requires: %{?scl_prefix_ror}rubygem(rails) < 4.2.7
Requires: %{?scl_prefix}rubygem(rest-client) >= 1.8.0
Requires: %{?scl_prefix}rubygem(rest-client) < 1.9.0
Requires: %{?scl_prefix}rubygem(audited-activerecord) >= 4.0
Requires: %{?scl_prefix}rubygem(audited-activerecord) < 5.0
Requires: %{?scl_prefix}rubygem(will_paginate) >= 3.0
Requires: %{?scl_prefix}rubygem(will_paginate) < 4.0
Requires: %{?scl_prefix}rubygem(ancestry) >= 2.0
Requires: %{?scl_prefix}rubygem(ancestry) < 3.0
Requires: %{?scl_prefix}rubygem(scoped_search) >= 3.2.2
Requires: %{?scl_prefix}rubygem(scoped_search) < 4.0
Requires: %{?scl_prefix}rubygem(ldap_fluff) >= 0.3.5
Requires: %{?scl_prefix}rubygem(ldap_fluff) < 1.0
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.3.4
Requires: %{?scl_prefix}rubygem(apipie-rails) < 0.4.0
Requires: %{?scl_prefix}rubygem(rabl) >= 0.11
Requires: %{?scl_prefix}rubygem(rabl) < 1.0
Requires: %{?scl_prefix}rubygem(oauth) >= 0.4
Requires: %{?scl_prefix}rubygem(oauth) < 1.0
Requires: %{?scl_prefix}rubygem(deep_cloneable) >= 2.0
Requires: %{?scl_prefix}rubygem(deep_cloneable) < 3.0
Requires: %{?scl_prefix}rubygem(validates_lengths_from_database) >= 0.5
Requires: %{?scl_prefix}rubygem(validates_lengths_from_database) < 1.0
Requires: %{?scl_prefix}rubygem(friendly_id) >= 5.0
Requires: %{?scl_prefix}rubygem(friendly_id) < 6.0
Requires: %{?scl_prefix}rubygem(secure_headers) >= 3.4
Requires: %{?scl_prefix}rubygem(secure_headers) < 4.0
Requires: %{?scl_prefix}rubygem(safemode) >= 1.2.4
Requires: %{?scl_prefix}rubygem(safemode) < 2.0
Requires: %{?scl_prefix}rubygem(fast_gettext) >= 0.8
Requires: %{?scl_prefix}rubygem(fast_gettext) < 1.2.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 1.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails) < 2.0
Requires: %{?scl_prefix}rubygem(rails-i18n) >= 4.0.0
Requires: %{?scl_prefix}rubygem(rails-i18n) < 4.1.0
Requires: %{?scl_prefix_ror}rubygem(turbolinks) >= 2.5
Requires: %{?scl_prefix_ror}rubygem(turbolinks) < 3.0
Requires: %{?scl_prefix}rubygem(logging) >= 1.8
Requires: %{?scl_prefix}rubygem(logging) < 3.0
Requires: %{?scl_prefix}rubygem(fog-core) = 1.42.0
Requires: %{?scl_prefix}rubygem(net-scp)
Requires: %{?scl_prefix}rubygem(net-ssh)
Requires: %{?scl_prefix}rubygem(net-ldap) >= 0.8.0
Requires: %{?scl_prefix}rubygem(activerecord-session_store) >= 0.1.1
Requires: %{?scl_prefix}rubygem(activerecord-session_store) < 2
Requires: %{?scl_prefix}rubygem(rails-observers) >= 0.1
Requires: %{?scl_prefix}rubygem(rails-observers) < 1.0
Requires: %{?scl_prefix_ror}rubygem(sprockets) >= 3
Requires: %{?scl_prefix_ror}rubygem(sprockets) < 4
Requires: %{?scl_prefix_ror}rubygem(sprockets-rails) >= 2.3.3
Requires: %{?scl_prefix_ror}rubygem(sprockets-rails) < 3
Requires: %{?scl_prefix}rubygem(responders) >= 2.0
Requires: %{?scl_prefix}rubygem(responders) < 3
Requires: %{?scl_prefix}rubygem(roadie-rails) >= 1.1
Requires: %{?scl_prefix}rubygem(roadie-rails) < 2
Requires: %{?scl_prefix}rubygem(x-editable-rails) >= 1.5.5
Requires: %{?scl_prefix}rubygem(x-editable-rails) < 1.6.0
Requires: %{?scl_prefix}rubygem(deacon) >= 1.0
Requires: %{?scl_prefix}rubygem(deacon) < 2.0
Requires: %{?scl_prefix}rubygem(webpack-rails) >= 0.9.7
Requires: %{?scl_prefix}rubygem(webpack-rails) < 1.0.0
# facter
%if 0%{?scl:1}
Requires: %{?scl_prefix}rubygem(facter)
%else
Requires: facter
%endif
# jsonp
Requires: %{?scl_prefix}rubygem(rack-jsonp)

# Build dependencies
BuildRequires: gettext
BuildRequires: asciidoc
BuildRequires: %{scl_ruby_bin}
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3
BuildRequires: %{?scl_prefix_ruby}rubygem(rdoc)
BuildRequires: %{?scl_prefix}rubygem(bundler_ext)
BuildRequires: %{?scl_prefix_ror}rubygem(sqlite3)
# Gemfile
BuildRequires: %{?scl_prefix_ror}rubygem(rails) >= 4.2.5.1
BuildRequires: %{?scl_prefix_ror}rubygem(rails) < 4.2.7
BuildRequires: %{?scl_prefix}rubygem(rest-client) >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(rest-client) < 1.9.0
BuildRequires: %{?scl_prefix}rubygem(audited-activerecord) >= 4.0
BuildRequires: %{?scl_prefix}rubygem(audited-activerecord) < 5.0
BuildRequires: %{?scl_prefix}rubygem(will_paginate) >= 3.0
BuildRequires: %{?scl_prefix}rubygem(will_paginate) < 4.0
BuildRequires: %{?scl_prefix}rubygem(ancestry) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(ancestry) < 3.0
BuildRequires: %{?scl_prefix}rubygem(scoped_search) >= 3.2.2
BuildRequires: %{?scl_prefix}rubygem(scoped_search) < 4.0
BuildRequires: %{?scl_prefix}rubygem(ldap_fluff) >= 0.3.5
BuildRequires: %{?scl_prefix}rubygem(ldap_fluff) < 1.0
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.3.4
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) < 0.4.0
BuildRequires: %{?scl_prefix}rubygem(rabl) >= 0.11
BuildRequires: %{?scl_prefix}rubygem(rabl) < 1.0
BuildRequires: %{?scl_prefix}rubygem(oauth) >= 0.4
BuildRequires: %{?scl_prefix}rubygem(oauth) < 1.0
BuildRequires: %{?scl_prefix}rubygem(deep_cloneable) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(deep_cloneable) < 3.0
BuildRequires: %{?scl_prefix}rubygem(validates_lengths_from_database) >= 0.5
BuildRequires: %{?scl_prefix}rubygem(validates_lengths_from_database) < 1.0
BuildRequires: %{?scl_prefix}rubygem(friendly_id) >= 5.0
BuildRequires: %{?scl_prefix}rubygem(friendly_id) < 6.0
BuildRequires: %{?scl_prefix}rubygem(secure_headers) >= 3.4
BuildRequires: %{?scl_prefix}rubygem(secure_headers) < 4.0
BuildRequires: %{?scl_prefix}rubygem(safemode) >= 1.2.4
BuildRequires: %{?scl_prefix}rubygem(safemode) < 2.0
BuildRequires: %{?scl_prefix}rubygem(fast_gettext) >= 0.8
BuildRequires: %{?scl_prefix}rubygem(fast_gettext) < 1.2.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails) < 2.0
BuildRequires: %{?scl_prefix}rubygem(rails-i18n) >= 4.0.0
BuildRequires: %{?scl_prefix}rubygem(rails-i18n) < 4.1.0
BuildRequires: %{?scl_prefix_ror}rubygem(turbolinks) >= 2.5
BuildRequires: %{?scl_prefix_ror}rubygem(turbolinks) < 3.0
BuildRequires: %{?scl_prefix}rubygem(logging) >= 1.8
BuildRequires: %{?scl_prefix}rubygem(logging) < 3.0
BuildRequires: %{?scl_prefix}rubygem(fog-core) = 1.42.0
BuildRequires: %{?scl_prefix}rubygem(net-scp)
BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix}rubygem(net-ldap) >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem(activerecord-session_store) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(activerecord-session_store) < 2
BuildRequires: %{?scl_prefix}rubygem(rails-observers) >= 0.1
BuildRequires: %{?scl_prefix}rubygem(rails-observers) < 1.0
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets) >= 3
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets) < 4
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets-rails) >= 2.3.3
BuildRequires: %{?scl_prefix_ror}rubygem(sprockets-rails) < 3
BuildRequires: %{?scl_prefix}rubygem(responders) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(responders) < 3
BuildRequires: %{?scl_prefix}rubygem(roadie-rails) >= 1.1
BuildRequires: %{?scl_prefix}rubygem(roadie-rails) < 2
BuildRequires: %{?scl_prefix}rubygem(x-editable-rails) >= 1.5.5
BuildRequires: %{?scl_prefix}rubygem(x-editable-rails) < 1.6.0
BuildRequires: %{?scl_prefix}rubygem(deacon) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(deacon) < 2.0
BuildRequires: %{?scl_prefix}rubygem(webpack-rails) >= 0.9.7
BuildRequires: %{?scl_prefix}rubygem(webpack-rails) < 1.0.0
# assets
%if 0%{?scl:1}
BuildRequires: %{scl}-runtime-assets >= 3
BuildRequires: %{scl}-runtime-assets < 4
%endif
BuildRequires: nodejs
# Temporary dep on libuv until https://bugs.centos.org/view.php?id=10606
# is resolved
BuildRequires: libuv
BuildRequires: npm(babel-core) < 6.8.0
BuildRequires: npm(babel-core) >= 6.7.2
BuildRequires: npm(babel-loader) < 6.3.0
BuildRequires: npm(babel-loader) >= 6.2.4
BuildRequires: npm(babel-plugin-transform-object-assign) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-assign) >= 6.8.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
BuildRequires: npm(babel-plugin-transform-object-rest-spread) >= 6.8.0
BuildRequires: npm(babel-preset-es2015) < 6.7.0
BuildRequires: npm(babel-preset-es2015) >= 6.6.0
BuildRequires: npm(babel-preset-react) < 7.0.0
BuildRequires: npm(babel-preset-react) >= 6.5.0
BuildRequires: npm(c3) >= 0.4.11
BuildRequires: npm(c3) < 1.0.0
BuildRequires: npm(css-loader) < 1.0.0
BuildRequires: npm(css-loader) >= 0.23.1
BuildRequires: npm(datatables.net) >= 1.10.12
BuildRequires: npm(datatables.net) < 1.11.0
BuildRequires: npm(datatables.net-bs) >= 1.10.12
BuildRequires: npm(datatables.net-bs) < 1.11.0
BuildRequires: npm(diff) >= 3.0.0
BuildRequires: npm(diff) < 3.1.0
BuildRequires: npm(es6-promise) < 4.0.0
BuildRequires: npm(es6-promise) >= 3.2.1
BuildRequires: npm(expose-loader) < 0.7.0
BuildRequires: npm(expose-loader) >= 0.6.0
BuildRequires: npm(extract-text-webpack-plugin) < 2.0.0
BuildRequires: npm(extract-text-webpack-plugin) >= 1.0.1
BuildRequires: npm(file-loader) < 1.0.0
BuildRequires: npm(file-loader) >= 0.9.0
BuildRequires: npm(flux) >= 2.1.1
BuildRequires: npm(flux) < 3.0.0
BuildRequires: npm(ipaddr.js) >= 1.2.0
BuildRequires: npm(ipaddr.js) < 1.3.0
BuildRequires: npm(jquery) < 1.12.0
BuildRequires: npm(jquery) >= 1.11.0
BuildRequires: npm(jquery-flot) < 0.9.0
BuildRequires: npm(jquery-flot) >= 0.8.3
BuildRequires: npm(jquery-ujs) < 1.3.0
BuildRequires: npm(jquery-ujs) >= 1.2.0
BuildRequires: npm(jquery.cookie) < 1.5.0
BuildRequires: npm(jquery.cookie) >= 1.4.1
BuildRequires: npm(jstz) < 1.1.0
BuildRequires: npm(jstz) >= 1.0.7
BuildRequires: npm(lodash) >= 4.15.0
BuildRequires: npm(lodash) < 4.16.0
BuildRequires: npm(multiselect) >= 0.9.12
BuildRequires: npm(multiselect) < 0.10.0
BuildRequires: npm(react) >= 15.1.0
BuildRequires: npm(react) < 16.0.0
BuildRequires: npm(react-bootstrap) >= 0.30.0
BuildRequires: npm(react-bootstrap) < 1.0.0
BuildRequires: npm(react-dom) >= 15.1.0
BuildRequires: npm(react-dom) < 16.0.0
BuildRequires: npm(select2) >= 3.5.2
BuildRequires: npm(select2) < 3.6.0
BuildRequires: npm(stats-webpack-plugin) < 1.0.0
BuildRequires: npm(stats-webpack-plugin) >= 0.2.1
BuildRequires: npm(style-loader) < 1.0.0
BuildRequires: npm(style-loader) >= 0.13.1
BuildRequires: npm(url-loader) < 1.0.0
BuildRequires: npm(url-loader) >= 0.5.7
BuildRequires: npm(webpack) < 2.0.0
BuildRequires: npm(webpack) >= 1.9.11
BuildRequires: nodejs-packaging
BuildRequires: %{?scl_prefix}rubygem(ace-rails-ap) >= 4.1.0
BuildRequires: %{?scl_prefix}rubygem(ace-rails-ap) < 4.2.0
BuildRequires: %{?scl_prefix_ror}rubygem(sass-rails) >= 5
BuildRequires: %{?scl_prefix_ror}rubygem(sass-rails) < 6
BuildRequires: %{?scl_prefix_ror}rubygem(uglifier) >= 1.0.3
BuildRequires: %{?scl_prefix_ror}rubygem(execjs) >= 1.4.0
BuildRequires: %{?scl_prefix_ror}rubygem(execjs) < 2.5.0
BuildRequires: %{?scl_prefix}rubygem(jquery-ui-rails) < 5.0.0
BuildRequires: %{?scl_prefix}rubygem(autoprefixer-rails) >= 5.2
BuildRequires: %{?scl_prefix}rubygem(autoprefixer-rails) < 6.0
BuildRequires: %{?scl_prefix}rubygem(patternfly-sass) >= 3.9
BuildRequires: %{?scl_prefix}rubygem(patternfly-sass) < 4.0
BuildRequires: %{?scl_prefix}rubygem(spice-html5-rails) >= 0.1.5
BuildRequires: %{?scl_prefix}rubygem(spice-html5-rails) < 0.2.0
BuildRequires: %{?scl_prefix}rubygem(quiet_assets) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(quiet_assets) < 2.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) < 2.0
BuildRequires: %{?scl_prefix}rubygem(gridster-rails) >= 0.5
BuildRequires: %{?scl_prefix}rubygem(gridster-rails) < 1.0
BuildRequires: %{?scl_prefix}rubygem(jquery_pwstrength_bootstrap_4) >= 1.2
BuildRequires: %{?scl_prefix}rubygem(jquery_pwstrength_bootstrap_4) < 2.0
BuildRequires: %{?scl_prefix}rubygem(jquery-turbolinks) >= 2.1
BuildRequires: %{?scl_prefix}rubygem(jquery-turbolinks) < 3.0
# facter
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix}rubygem(facter)
%else
BuildRequires: facter
%endif

%package cli
Summary: Foreman CLI
Group: Applications/System
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman)

%description cli
Meta Package to install hammer rubygems and its dependencies

%files cli

%package debug
Summary: Foreman debug utilities
Group: Applications/System
Requires: rsync

%description debug
Useful utilities for debug info collection

%files debug
%{_sbindir}/%{name}-debug
%{_datadir}/%{name}/script/%{name}-debug.d

%package release
Summary:        Foreman repository files
Group:  	Applications/System


%description release
Foreman repository contains open source and other distributable software for
distributions in RPM format. This package contains the repository configuration
for Yum.

%files release
%config %{_sysconfdir}/yum.repos.d/*
/etc/pki/rpm-gpg/*
%{_sysconfdir}/rpm/macros.%{name}-dist

%package libvirt
Summary: Foreman libvirt support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog-libvirt) >= 0.0.2
Requires: %{?scl_prefix}rubygem(fog-libvirt) < 1.0
Requires: %{?scl_prefix}rubygem(ruby-libvirt) >= 0.4
Requires: %{?scl_prefix}rubygem(ruby-libvirt) < 1.0
Requires: %{name} = %{version}-%{release}
Obsoletes: foreman-virt < 1.0.0
Provides: foreman-virt = 1.0.0

%description libvirt
Meta package to install requirements for libvirt compute resource support.

%files libvirt
%{_datadir}/%{name}/bundler.d/libvirt.rb

%package openstack
Summary: Foreman OpenStack support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog-openstack) >= 0.1.11
Requires: %{?scl_prefix}rubygem(fog-openstack) < 1.0
Requires: %{name} = %{version}-%{release}

%description openstack
Meta package to install requirements for OpenStack compute resource support.

%files openstack
%{_datadir}/%{name}/bundler.d/openstack.rb

%package ovirt
Summary: Foreman oVirt support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(rbovirt) >= 0.1.1
Requires: %{?scl_prefix}rubygem(rbovirt) < 0.2.0
Requires: foreman-compute = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description ovirt
Meta package to install requirements for oVirt compute resource support.

%files ovirt
%{_datadir}/%{name}/bundler.d/ovirt.rb

%package compute
Summary: Foreman compute resource Fog dependencies
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog) = 1.38.0
Requires: %{name} = %{version}-%{release}
Obsoletes: foreman-compute < 1.8.0
Obsoletes: foreman-fog < 1.0.0
Provides: foreman-fog = 1.0.0
Obsoletes: foreman-ec2 < 1.3.0

%description compute
Meta package to install dependencies to support some compute resources. Most
compute resources have a more specific package which should be installed in
preference to this package.

%files compute
%{_datadir}/%{name}/bundler.d/fog.rb

%package ec2
Summary:   Foreman Amazon Web Services (AWS) EC2 support
Group:     Applications/System
Requires:  %{?scl_prefix}rubygem(fog-aws) >= 0.1.0
Requires:  %{?scl_prefix}rubygem(fog-aws) < 1.0.0
Requires:  %{name} = %{version}-%{release}

%description ec2
Meta package to install requirements for Amazon Web Services (AWS) EC2 support.

%files ec2
%{_datadir}/%{name}/bundler.d/ec2.rb

%package rackspace
Summary: Foreman Rackspace support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog-rackspace) >= 0.1
Requires: %{?scl_prefix}rubygem(fog-rackspace) < 1.0
Requires: %{name} = %{version}-%{release}

%description rackspace
Meta package to install requirements for Rackspace compute resource support.

%files rackspace
%{_datadir}/%{name}/bundler.d/rackspace.rb

%package vmware
Summary: Foreman VMware support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog-vsphere) >= 0.6.2
Requires: %{name} = %{version}-%{release}

%description vmware
Meta package to install requirements for VMware compute resource support.

%files vmware
%{_datadir}/%{name}/bundler.d/vmware.rb

%package gce
Summary: Foreman Google Compute Engine (GCE) support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(fog-google) >= 0.0
Requires: %{?scl_prefix}rubygem(fog-google) <= 0.1.0
Requires: %{?scl_prefix}rubygem(google-api-client) >= 0.8.2
Requires: %{?scl_prefix}rubygem(google-api-client) < 0.9.0
Requires: %{?scl_prefix}rubygem(sshkey) >= 1.3
Requires: %{?scl_prefix}rubygem(sshkey) < 2.0
Requires: %{name} = %{version}-%{release}

%description gce
Meta package to install requirements for Google Compute Engine (GCE) support

%files gce
%{_datadir}/%{name}/bundler.d/gce.rb

%package assets
Summary: Foreman asset pipeline support
Group: Applications/system
Requires: %{name} = %{version}-%{release}
%if 0%{?scl:1}
Requires: %{scl}-runtime-assets >= 3
Requires: %{scl}-runtime-assets < 4
%endif
Requires: nodejs
# Temporary dep on libuv until https://bugs.centos.org/view.php?id=10606
# is resolved
Requires: libuv
Requires: npm(babel-core) < 6.8.0
Requires: npm(babel-core) >= 6.7.2
Requires: npm(babel-loader) < 6.3.0
Requires: npm(babel-loader) >= 6.2.4
Requires: npm(babel-plugin-transform-object-assign) < 7.0.0
Requires: npm(babel-plugin-transform-object-assign) >= 6.8.0
Requires: npm(babel-plugin-transform-object-rest-spread) < 7.0.0
Requires: npm(babel-plugin-transform-object-rest-spread) >= 6.8.0
Requires: npm(babel-preset-es2015) < 6.7.0
Requires: npm(babel-preset-es2015) >= 6.6.0
Requires: npm(babel-preset-react) < 7.0.0
Requires: npm(babel-preset-react) >= 6.5.0
Requires: npm(c3) >= 0.4.11
Requires: npm(c3) < 1.0.0
Requires: npm(css-loader) < 1.0.0
Requires: npm(css-loader) >= 0.23.1
Requires: npm(datatables.net) >= 1.10.12
Requires: npm(datatables.net) < 1.11.0
Requires: npm(datatables.net-bs) >= 1.10.12
Requires: npm(datatables.net-bs) < 1.11.0
Requires: npm(diff) >= 3.0.0
Requires: npm(diff) < 3.1.0
Requires: npm(es6-promise) < 4.0.0
Requires: npm(es6-promise) >= 3.2.1
Requires: npm(expose-loader) < 0.7.0
Requires: npm(expose-loader) >= 0.6.0
Requires: npm(extract-text-webpack-plugin) < 2.0.0
Requires: npm(extract-text-webpack-plugin) >= 1.0.1
Requires: npm(file-loader) < 1.0.0
Requires: npm(file-loader) >= 0.9.0
Requires: npm(flux) >= 2.1.1
Requires: npm(flux) < 3.0.0
Requires: npm(ipaddr.js) >= 1.2.0
Requires: npm(ipaddr.js) < 1.3.0
Requires: npm(jquery) < 1.12.0
Requires: npm(jquery) >= 1.11.0
Requires: npm(jquery-flot) < 0.9.0
Requires: npm(jquery-flot) >= 0.8.3
Requires: npm(jquery-ujs) < 1.3.0
Requires: npm(jquery-ujs) >= 1.2.0
Requires: npm(jquery.cookie) < 1.5.0
Requires: npm(jquery.cookie) >= 1.4.1
Requires: npm(jstz) < 1.1.0
Requires: npm(jstz) >= 1.0.7
Requires: npm(lodash) >= 4.15.0
Requires: npm(lodash) < 4.16.0
Requires: npm(multiselect) >= 0.9.12
Requires: npm(multiselect) < 0.10.0
Requires: npm(react) >= 15.1.0
Requires: npm(react) < 16.0.0
Requires: npm(react-bootstrap) >= 0.30.0
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(react-dom) >= 15.1.0
Requires: npm(react-dom) < 16.0.0
Requires: npm(select2) >= 3.5.2
Requires: npm(select2) < 3.6.0
Requires: npm(stats-webpack-plugin) < 1.0.0
Requires: npm(stats-webpack-plugin) >= 0.2.1
Requires: npm(style-loader) < 1.0.0
Requires: npm(style-loader) >= 0.13.1
Requires: npm(url-loader) < 1.0.0
Requires: npm(url-loader) >= 0.5.7
Requires: npm(webpack) < 2.0.0
Requires: npm(webpack) >= 1.9.11
Requires: %{?scl_prefix}rubygem(ace-rails-ap) >= 4.1.0
Requires: %{?scl_prefix}rubygem(ace-rails-ap) < 4.2.0
Requires: %{?scl_prefix_ror}rubygem(sass-rails) >= 5
Requires: %{?scl_prefix_ror}rubygem(sass-rails) < 6
Requires: %{?scl_prefix_ror}rubygem(uglifier) >= 1.0.3
Requires: %{?scl_prefix_ror}rubygem(execjs) >= 1.4.0
Requires: %{?scl_prefix}rubygem(jquery-ui-rails) < 5.0.0
Requires: %{?scl_prefix}rubygem(autoprefixer-rails) >= 5.2
Requires: %{?scl_prefix}rubygem(autoprefixer-rails) < 6.0
Requires: %{?scl_prefix}rubygem(patternfly-sass) >= 3.9
Requires: %{?scl_prefix}rubygem(patternfly-sass) < 4.0
Requires: %{?scl_prefix}rubygem(spice-html5-rails) >= 0.1.5
Requires: %{?scl_prefix}rubygem(spice-html5-rails) < 0.2.0
Requires: %{?scl_prefix}rubygem(quiet_assets) >= 1.0
Requires: %{?scl_prefix}rubygem(quiet_assets) < 2.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) >= 1.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails_js) < 2.0
Requires: %{?scl_prefix}rubygem(gridster-rails) >= 0.5
Requires: %{?scl_prefix}rubygem(gridster-rails) < 1.0
Requires: %{?scl_prefix}rubygem(jquery_pwstrength_bootstrap_4) >= 1.2
Requires: %{?scl_prefix}rubygem(jquery_pwstrength_bootstrap_4) < 2.0
Requires: %{?scl_prefix}rubygem(jquery-turbolinks) >= 2.1
Requires: %{?scl_prefix}rubygem(jquery-turbolinks) < 3.0

%description assets
Meta package to install asset pipeline support.

%files assets
%{_datadir}/%{name}/bundler.d/assets.rb

%package plugin
Summary: Foreman plugin support
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-release = %{version}-%{release}
Requires: %{name}-sqlite = %{version}-%{release}

%description plugin
Meta package with support for plugins.

%files plugin
%{_sysconfdir}/rpm/macros.%{name}-plugin


%package console
Summary: Foreman console support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(wirb) >= 1.0
Requires: %{?scl_prefix}rubygem(wirb) < 3.0
Requires: %{?scl_prefix}rubygem(hirb-unicode-steakknife) >= 0.0.7
Requires: %{?scl_prefix}rubygem(hirb-unicode-steakknife) < 0.1
Requires: %{?scl_prefix}rubygem(awesome_print) >= 1.0
Requires: %{?scl_prefix}rubygem(awesome_print) < 2.0
Requires: %{name} = %{version}-%{release}

%description console
Meta Package to install requirements for console support

%files console
%{_datadir}/%{name}/bundler.d/console.rb

%package mysql2
Summary: Foreman mysql2 support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(mysql2) >= 0.3.13
Requires: %{?scl_prefix}rubygem(mysql2) < 0.5.0
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-mysql < 1.4.0
Provides: %{name}-mysql = %{version}

%description mysql2
Meta Package to install requirements for mysql2 support

%files mysql2
%{_datadir}/%{name}/bundler.d/mysql2.rb

%package postgresql
Summary: Foreman Postgresql support
Group:  Applications/System
Requires: %{?scl_prefix}rubygem(pg) >= 0.15.0
Requires: %{?scl_prefix}rubygem(pg) < 1.0
Requires: %{name} = %{version}-%{release}

%description postgresql
Meta Package to install requirements for postgresql support

%files postgresql
%{_datadir}/%{name}/bundler.d/postgresql.rb

%package sqlite
Summary: Foreman sqlite support
Group:  Applications/System
Requires: %{?scl_prefix_ror}rubygem(sqlite3) >= 1.3.6
Requires: %{?scl_prefix_ror}rubygem(sqlite3) < 1.4.0
Requires: %{name} = %{version}-%{release}

%description sqlite
Meta Package to install requirements for sqlite support

%files sqlite
%{_datadir}/%{name}/bundler.d/sqlite.rb

%description
Foreman is aimed to be a Single Address For All Machines Life Cycle Management.
Foreman is based on Ruby on Rails, and this package bundles Rails and all
plugins required for Foreman to work.

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
#build man pages
%{scl_rake} -f Rakefile.dist build \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

#replace shebangs and binaries in scripts for SCL
%if %{?scl:1}%{!?scl:0}
  # shebangs
  for f in extras/rdoc/rdoc_prepare_script.rb \
  bin/* script/performance/profiler script/performance/benchmarker script/foreman-config ; do
    sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby_bin}X' $f
  done
  sed -ri '1,$sX/usr/bin/rubyX%{scl_ruby_bin}X' %{SOURCE1}
  # script content
  sed -ri 'sX/usr/bin/rakeX%{scl_rake}X' extras/dbmigrate script/foreman-rake
%endif

#build locale files
make -C locale all-mo

#use Bundler_ext instead of Bundler
mv Gemfile Gemfile.in
cp config/database.yml.example config/database.yml
cp config/settings.yaml.example config/settings.yaml
#we need to allow taxonomies so apipie cache renders documentation with them
sed -i 's/:locations_enabled: false/:locations_enabled: true/' config/settings.yaml
sed -i 's/:organizations_enabled: false/:organizations_enabled: true/' config/settings.yaml
export BUNDLER_EXT_GROUPS="default assets"
ln -s %{nodejs_sitelib} node_modules
export NODE_ENV=production
webpack.js --bail --config config/webpack.config.js
%{scl_rake} assets:precompile RAILS_ENV=production --trace
%{scl_rake} db:migrate RAILS_ENV=production --trace
%{scl_rake} apipie:cache RAILS_ENV=production cache_part=resources --trace
rm config/database.yml config/settings.yaml

%install
rm -rf %{buildroot}

#install man pages
%{scl_rake} -f Rakefile.dist install \
  PREFIX=%{buildroot}%{_prefix} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace
%{scl_rake} -f Rakefile.dist clean

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/plugins
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp/pids
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}/plugins
install -Dp -m0755 script/%{name}-debug %{buildroot}%{_sbindir}/%{name}-debug
install -Dp -m0755 script/%{name}-rake %{buildroot}%{_sbindir}/%{name}-rake
install -Dp -m0755 script/%{name}-tail %{buildroot}%{_sbindir}/%{name}-tail
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/cron.d/%{name}
%if 0%{?rhel} > 6 || 0%{?fedora} > 16
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
%endif

install -Dpm0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/yum.repos.d/%{name}.repo
install -Dpm0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/yum.repos.d/%{name}-plugins.repo
sed "s/\$DIST/$(echo %{?dist} | cut -d. -f2)/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/%{name}*.repo
install -Dpm0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman

cp -p Gemfile.in %{buildroot}%{_datadir}/%{name}/Gemfile.in
cp -p -r app bin bundler.d config config.ru extras lib locale Rakefile script %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/extras/{jumpstart,spec}

# remove all test units from produciton release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# Move config files to %{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/config/database.yml.example %{buildroot}%{_datadir}/%{name}/config/database.yml
mv %{buildroot}%{_datadir}/%{name}/config/email.yaml.example %{buildroot}%{_datadir}/%{name}/config/email.yaml
mv %{buildroot}%{_datadir}/%{name}/config/settings.yaml.example %{buildroot}%{_datadir}/%{name}/config/settings.yaml

for i in database.yml email.yaml logging.yaml settings.yaml foreman-debug.conf; do
mv %{buildroot}%{_datadir}/%{name}/config/$i %{buildroot}%{_sysconfdir}/%{name}
ln -sv %{_sysconfdir}/%{name}/$i %{buildroot}%{_datadir}/%{name}/config/$i
done

# Put db in %{_localstatedir}/lib/%{name}/db
cp -pr db/migrate db/seeds.rb db/seeds.d %{buildroot}%{_datadir}/%{name}
mkdir %{buildroot}%{_localstatedir}/lib/%{name}/db

ln -sv %{_localstatedir}/lib/%{name}/db %{buildroot}%{_datadir}/%{name}/db
ln -sv %{_datadir}/%{name}/migrate %{buildroot}%{_localstatedir}/lib/%{name}/db/migrate
ln -sv %{_datadir}/%{name}/seeds.rb %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.rb
ln -sv %{_datadir}/%{name}/seeds.d %{buildroot}%{_localstatedir}/lib/%{name}/db/seeds.d

# Put HTML %{_localstatedir}/lib/%{name}/public
cp -pr public %{buildroot}%{_localstatedir}/lib/%{name}/
ln -sv %{_localstatedir}/lib/%{name}/public %{buildroot}%{_datadir}/%{name}/public

# Put logs in %{_localstatedir}/log/%{name}
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{_datadir}/%{name}/log

# Put tmp files in %{_localstatedir}/run/%{name}
ln -sv %{_localstatedir}/run/%{name} %{buildroot}%{_datadir}/%{name}/tmp

# Symlink plugin settings directory to
ln -sv %{_sysconfdir}/%{name}/plugins %{buildroot}%{_datadir}/%{name}/config/settings.plugins.d

# Create VERSION file
install -pm0644 VERSION %{buildroot}%{_datadir}/%{name}/VERSION

# Create RPM macros for plugin packages to use at build time
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name} << EOF
# Common locations
%%%{name}_dir %{_datadir}/%{name}
%%%{name}_bundlerd_dir %%{%{name}_dir}/bundler.d
%%%{name}_log_dir %{_localstatedir}/log/%{name}

# Common commands
%%%{name}_rake         %{foreman_rake}
%%%{name}_db_migrate   %%{%{name}_rake} db:migrate >> %%{%{name}_log_dir}/db_migrate.log 2>&1 || :
%%%{name}_db_seed      %%{%{name}_rake} db:seed >> %%{%{name}_log_dir}/db_seed.log 2>&1 || :
%%%{name}_restart      (/sbin/service %{name} status && /sbin/service %{name} restart) >/dev/null 2>&1
EOF

cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name}-dist << EOF
# Version to use like a dist tag
%%%{name}dist .fm$(echo %{version} | awk -F. '{print $1 "_" $2}')
EOF

cat > %{buildroot}%{_sysconfdir}/rpm/macros.%{name}-plugin << EOF
# Generate bundler.d file for a plugin
# -n<plugin_name>   Overrides default of gem_name
%%%{name}_bundlerd_file(n:) \\
mkdir -p %%{buildroot}%%{%{name}_bundlerd_dir} \\
cat <<GEMFILE > %%{buildroot}%%{%{name}_bundlerd_dir}/%%{-n*}%%{!?-n:%%{gem_name}}.rb \\
gem '%%{-n*}%%{!?-n:%%{gem_name}}' \\
GEMFILE

# Common locations
%%%{name}_bundlerd_plugin %%{%{name}_bundlerd_dir}/%%{gem_name}.rb
%%%{name}_pluginconf_dir %{_sysconfdir}/%{name}/plugins
# Common assets locations
%%%{name}_assets_plugin %%{gem_instdir}/public/assets/%%{gem_name}
# Common apipie locations
%%%{name}_apipie_cache_plugin %%{gem_instdir}/public/apipie-cache/plugin/%%{gem_name}
%%%{name}_apipie_cache_foreman %%{foreman_dir}/public/apipie-cache/plugin/%%{gem_name}
# build apipie cache index
%%%{name}_apipie_cache %%{%{name}_rake} apipie:cache:index >> %%{%{name}_log_dir}/apipie_cache.log 2>&1 || :

# Generate precompiled assets at gem_instdir/public/assets/gem_name/
# -r<rake_task>     Overrides rake task of plugin:assets:precompile[plugin_name]
# -n<plugin_name>   Overrides default of gem_name for precompile step
# -a                Prebuild apipie cache
# -s                Precompile assets
%%%{name}_precompile_plugin(r:n:as) \\
mkdir -p ./%{_datadir} \\
cp -r %%{%{name}_dir} ./%{_datadir} || echo 0 \\
mkdir -p ./%{_localstatedir}/lib/%{name} \\
cp -r %{_localstatedir}/lib/%{name}/db ./%{_localstatedir}/lib/%{name} || echo 0 \\
unlink ./%{_datadir}/%{name}/db \\
ln -sv \`pwd\`/%{_localstatedir}/lib/%{name}/db ./%{_datadir}/%{name}/db \\
pushd ./%%{%{name}_dir} \\
\\
sed -i 's/:locations_enabled: false/:locations_enabled: true/' \`pwd\`/config/settings.yaml \\
sed -i 's/:organizations_enabled: false/:organizations_enabled: true/' \`pwd\`/config/settings.yaml \\
export GEM_PATH=%%{buildroot}%%{gem_dir}:\${GEM_PATH:+\${GEM_PATH}}\${GEM_PATH:-\`%{?scl:scl enable %%{scl_ror} -- }ruby -e "print Gem.path.join(':')"\`} \\
cp %%{buildroot}%%{%{name}_bundlerd_dir}/%%{gem_name}.rb ./bundler.d/%%{gem_name}.rb \\
unlink tmp \\
\\
rm \`pwd\`/config/initializers/encryption_key.rb \\
/usr/bin/%%{?scl:%%{scl}-}rake security:generate_encryption_key \\
export BUNDLER_EXT_NOSTRICT=1 \\
%%{?-s:/usr/bin/%%{?scl:%%{scl}-}rake %%{-r*}%%{!?-r:plugin:assets:precompile[%%{-n*}%%{!?-n:%%{gem_name}}]} RAILS_ENV=production --trace} \\
%%{?-a:/usr/bin/%%{?scl:%%{scl}-}rake db:migrate RAILS_ENV=development --trace} \\
%%{?-a:/usr/bin/%%{?scl:%%{scl}-}rake plugin:apipie:cache[%%{gem_name}] RAILS_ENV=development cache_part=resources OUT=%%{buildroot}%%{gem_instdir}/public/apipie-cache/plugin/%%{gem_name} --trace} \\
\\
popd \\
rm -rf ./usr \\
%%{?-a:mkdir -p %%{buildroot}%%{foreman_dir}/public/apipie-cache/plugin} \\
%%{?-a:ln -s %%{gem_instdir}/public/apipie-cache/plugin/%%{gem_name} %%{buildroot}%%{foreman_dir}/public/apipie-cache/plugin/%%{gem_name}}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGELOG Contributors LICENSE README.md VERSION
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/app
%exclude %{_datadir}/%{name}/app/assets
%exclude %{_datadir}/%{name}/script/%{name}-debug.d
%dir %{_datadir}/%{name}/bundler.d
%exclude %{_datadir}/%{name}/bundler.d/development.rb
%{_datadir}/%{name}/bundler.d/facter.rb
%{_datadir}/%{name}/bundler.d/jsonp.rb
%exclude %{_datadir}/%{name}/bundler.d/openid.rb
%exclude %{_datadir}/%{name}/bundler.d/test.rb
%{_datadir}/%{name}/bin
%{_datadir}/%{name}/config*
%{_datadir}/%{name}/db
%{_datadir}/%{name}/extras
%{_datadir}/%{name}/Gemfile.in
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/locale
%{_datadir}/%{name}/log
%{_datadir}/%{name}/migrate
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/public
%{_datadir}/%{name}/Rakefile
%{_datadir}/%{name}/script
%{_datadir}/%{name}/seeds.*
%attr(700,%{name},%{name}) %{_datadir}/%{name}/.ssh
%{_datadir}/%{name}/tmp
%{_datadir}/%{name}/VERSION
%{_initrddir}/%{name}
%{_sbindir}/%{name}-rake
%{_sbindir}/%{name}-tail
%{_mandir}/man8
%config(noreplace) %{_sysconfdir}/%{name}
%ghost %attr(0640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/encryption_key.rb
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config %{_sysconfdir}/cron.d/%{name}
%{_sysconfdir}/rpm/macros.%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}
%attr(750,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(750,%{name},%{name}) %{_localstatedir}/log/%{name}/plugins
%attr(-,%{name},%{name}) %{_localstatedir}/run/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%attr(-,%{name},root) %{_datadir}/%{name}/config/environment.rb
# Symlink to /etc, EL6 needs attrs for ghost files, Fedora doesn't
%if 0%{?rhel} == 6
%ghost %attr(0777,root,root) %{_datadir}/%{name}/config/initializers/encryption_key.rb
%else
%ghost %{_datadir}/%{name}/config/initializers/encryption_key.rb
%endif
%ghost %attr(0640,root,%{name}) %config(noreplace) %{_datadir}/%{name}/config/initializers/local_secret_token.rb
# Only need tmpfiles on systemd (F17 and up)
%if 0%{?rhel} > 6 || 0%{?fedora} > 16
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%endif

%pre
# Add the "foreman" user and group
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{homedir} -s /sbin/nologin -c "Foreman" %{name}
exit 0

%post
# secret token used for cookie signing etc.
if [ ! -f %{_datadir}/%{name}/config/initializers/local_secret_token.rb ]; then
  touch %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  chmod 0660 %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  chgrp foreman %{_datadir}/%{name}/config/initializers/local_secret_token.rb
  %{foreman_rake} security:generate_token >/dev/null 2>&1 || :
  chmod 0640 %{_datadir}/%{name}/config/initializers/local_secret_token.rb
fi

# encryption key used to encrypt DB contents
# move the generated key file to /etc/foreman/ so users back it up, symlink to it from ~foreman
if [ ! -e %{_datadir}/%{name}/config/initializers/encryption_key.rb -a \
     ! -e %{_sysconfdir}/%{name}/encryption_key.rb ]; then
  touch %{_datadir}/%{name}/config/initializers/encryption_key.rb
  chmod 0660 %{_datadir}/%{name}/config/initializers/encryption_key.rb
  chgrp foreman %{_datadir}/%{name}/config/initializers/encryption_key.rb
  %{foreman_rake} security:generate_encryption_key >/dev/null 2>&1 || :
  chmod 0640 %{_datadir}/%{name}/config/initializers/encryption_key.rb
  mv %{_datadir}/%{name}/config/initializers/encryption_key.rb %{_sysconfdir}/%{name}/
fi
if [ ! -e %{_datadir}/%{name}/config/initializers/encryption_key.rb -a \
     -e %{_sysconfdir}/%{name}/encryption_key.rb ]; then
  ln -s %{_sysconfdir}/%{name}/encryption_key.rb %{_datadir}/%{name}/config/initializers/
fi

/sbin/chkconfig --add %{name} || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%posttrans
# We need to run the db:migrate after the install transaction
# always attempt to reencrypt after update in case new fields can be encrypted
%{foreman_rake} db:migrate db:encrypt_all >> %{_localstatedir}/log/%{name}/db_migrate.log 2>&1 || :
%{foreman_rake} db:seed >> %{_localstatedir}/log/%{name}/db_seed.log 2>&1 || :
%{foreman_rake} apipie:cache:index >> %{_localstatedir}/log/%{name}/apipie_cache.log 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%preun
if [ $1 -eq 0 ] ; then
/sbin/service %{name} stop >/dev/null 2>&1
/sbin/chkconfig --del %{name} || :
fi

%postun
if [ $1 -ge 1 ] ; then
# Restart the service
/sbin/service %{name} restart >/dev/null 2>&1 || :
fi

%changelog
* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> - 1.14.0-0.develop
- Bump version to 1.14-develop

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> - 1.13.0-0.develop
- Bump version to 1.13-develop

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> - 1.12.0-0.develop
- Bump version to 1.12-develop

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> - 1.11.0-0.develop
- Bump version to 1.11-develop

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> - 1.10.0-0.develop
- Bump version to 1.10-develop

* Tue Mar 03 2015 Dominic Cleal <dcleal@redhat.com> - 1.9.0-0.develop
- Bump version to 1.9-develop

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> - 1.8.0-0.develop
- Bump version to 1.8-develop

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> - 1.7.0-0.develop
- Bump version to 1.7-develop

* Wed Apr 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.6.0-0.develop
- Bump version to 1.6-develop

* Thu Jan 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.5.0-0.develop
- Bump version to 1.5-develop
- Remove rails3_before_render dependency
- generate encryption key and encrypt data in postinstall (#2929)

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> - 1.4.0-0.develop
- Bump and change versioning scheme, don't overwrite VERSION (#3712)
- Pin fog to 1.18.x
- Add new rails3_before_render dependency
- Removed foreman-mysql package (obsoleted by mysql2)
- Seed database after DB migration
- Change twitter-bootstrap-rails to bootstrap-sass
- Pin fog to 1.19.x
- Add BR and explicit dependency on Ruby binary, for ruby193-ruby-wrapper

* Tue Nov 12 2013 Sam Kottler <shk@redhat.com> - 1.3.9999-7
- Add rubygem-unf as a requires for the compute subpackage

* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> - 1.3.9999-6
* Add foreman-gce subpackage for Google Compute Engine

* Wed Nov 6 2013 David Davis <daviddavis@redhat.com> - 1.3.9999-5
- Removing rr gem, fixes #3597

* Fri Oct 25 2013 Martin Bacovsky <mbacovsk@redhat.com> - 1.3.9999-4
- foreman-cli metapackage installs hammer

* Mon Sep 30 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-3
- Adding Foreman plugins repo

* Fri Sep 27 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-2
- Update rubygem-ancestry to 2.x

* Wed Sep 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-1
- Bump to version 1.3-develop

* Wed Sep 11 2013 Dominic Cleal <dcleal@redhat.com> - 1.2.9999-11
- Add new foreigner and immigrant dependencies

* Mon Sep 09 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-10
- Added dependency on fast_gettext 0.8 (multi-domain support)

* Mon Sep 02 2013 Greg Sutcliffe <gsutclif@redhat.com> 1.2.9999-9
- Remove Puppet from core requirements

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.2.9999-8
- Update fog dependency to 1.15.0 to fix rackspace VM listing issue

* Wed Jul 24 2013 Jason Montleon <jmontleo@redhat.com> 1.2.9999-7
- Update rbovirt dependency version to 0.0.21 to support sending the host ssl certificate subject as an option to the xpi plugin

* Fri Jul 19 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-6
- add foreman-rake to /usr/sbin

* Mon Jun 17 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-5
- fix asset dependency versions
- add minitest dependency for console (Lukas Zapletal)

* Thu Jun 06 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-4
- fix libvirt package dependency on ruby-libvirt

* Wed Jun 05 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-3
- foreman-debug tool now installed into /usr/sbin

* Tue May 28 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-2
- Don't force SCL
- Distribute GPG key
- Replace dist in foreman.repo
- Rename foreman-ec2 to foreman-compute
- Update dbmigrate for SCL (Lukas Zapletal)

* Mon May 20 2013 Dominic Cleal <dcleal@redhat.com> 1.2.9999-1
- Updated to 1.2.9999 (1.3-pre)

* Tue Apr 30 2013 Sam Kottler <shk@redhat.com> 1.1.9999-1
- Updated to 1.1.9999 (1.2-pre)

* Fri Feb 15 2013 shk@redhat.com 1.1-3
- Bumped safemode dependency

* Thu Feb 14 2013 shk@redhat.com 1.1-2
- Fixed baseurl in the -release subpackage.
- Updated to 1.1-1

* Mon Feb 4 2013 shk@redhat.com 1.1-1
- 1.1 final.

* Mon Jan 28 2013 shk@redhat.com 1.1RC5-2
- Bumped fog version dependency

* Fri Jan 25 2013 shk@redhat.com 1.1RC5-1
- Updated Rails requirements and bumped to RC5.

* Thu Dec 27 2012 shk@redhat.com 1.1RC3-1
- Updated to 1.1RC3 and updated dependencies.

* Wed Dec 19 2012 jmontleo@redhat.com 1.0.2-1
- Fix Foreman SQL injection through search mechanism CVE-2012-5648

* Thu Aug 09 2012 jmontleo@redhat.com 1.0.1-1
- Version 1.0.1

* Sun Aug 05 2012 jmontleo@redhat.com 1.0.0-2
- Update to pull in fixes

* Mon Jul 23 2012 jmontleo@redhat.com 1.0.0-1
- Update packages for Foreman 1.0 Release and add support for using thin.

* Wed Jul 18 2012 jmontleo@redhat.com 1.0.0-0.7
- Updated pacakages for Foreman 1.0 RC5 and Proxy RC2

* Thu Jul 05 2012 jmontleo@redhat.com 1.0.0-0.6
- Fix foreman-release to account for different archs. Pull todays source.

* Wed Jul 04 2012 jmontleo@redhat.com 1.0.0-0.5
- Bump version number and rebuild for RC3

* Sun Jul 01 2012 jmontleo@redhat.com 1.0.0-0.4
- Pull todays develop branch to fix dbmigrate issue, add mistakenly deleted version string back, and replace foreman-fog with foreman-ec2 as it indicates more clearly what functionality the package provides.

* Fri Jun 29 2012 jmontleo@redhat.com 1.0.0-0.3
- More fixes for dbmigrate, foreman-cli and foreman-release added

* Fri Jun 29 2012 jmontleo@redhat.com 1.0.0-0.2
- Rebuild with develop branch from today for 1.0.0 RC2. Try to fix inconsistent db:migrate runs on upgrades.

* Tue Jun 19 2012 jmontleo@redhat.com 0-5.1-20
- Implement conf.d style Gemfile configuration for bundle to replace the ugly method used in previous rpm versions. Replace foreman-virt package with foreman-libvirt package as it was confusing to have fog virt ovirt and vmware.

* Tue Jun 19 2012 jmontleo@redhat.com 0-5.1-9
- Rebuild with todays develop branch. Add VERSION file 1688, add wget dependency 1514, update rbovirt dep to 0.0.12, and break out ovirt support to foreman-ovirt package.

* Thu Jun 14 2012 jmontleo@redhat.com 0.5.1-8
- Rebuild with todays develop branch.

* Wed Jun 13 2012 jmontleo@redhat.com 0.5.1-7
- Rebuild with todays develop branch. Add require for at least rubygem-rake 0.9.2.2. Run rake:db migrate on upgrade.

* Wed May 30 2012 jmontleo@redhat.com 0.5.1-5
- Rebuild with todays merge of compute resource RBAC patch

* Tue May 29 2012 jmontleo@redhat.com 0.5.1-4
- Fix rpm dependencies for foreman-virt and foreman-vmware to include foreman-fog

* Tue May 29 2012 jmontleo@redhat.com 0.5.1-3
- tidy up postinstall prepbundle.sh, rebuild with EC2 support, and split out foreman-fog and foreman-vmware support

* Tue May 08 2012 jmontleo@redhat.com 0.5.1-1
- adding prepbundle.sh to run post install of any foreman packages, other small fixes

* Fri May 04 2012 jmontleo@redhat.com 0.5.1-0.2
- updated foreman to develop branch from May 04 which included many fixes including no longer requiring foreman-virt

* Wed Jan 11 2012 ohadlevy@gmail.com - 0.4.2
- rebuilt

* Tue Dec 6 2011 ohadlevy@gmail.com - 0.4.1
- rebuilt

* Tue Nov 08 2011 ohadlevy@gmail.com - 0.4
- rebuilt

* Mon Nov 07 2011 ohadlevy@gmail.com - 0.4rc5
- rebuilt

* Tue Oct 25 2011 ohadlevy@gmail.com - 0.4rc4
- rebuilt

* Tue Oct 18 2011 ohadlevy@gmail.com - 0.4rc3
- rebuilt

* Wed Sep 28 2011 ohadlevy@gmail.com - 0.4rc2
- rebuilt

* Sat Sep 10 2011 ohadlevy@gmail.com - 0.4rc1
- rebuilt

* Tue Jun 07 2011 ohadlevy@gmail.com - 0.3
- rebuilt

* Tue May 24 2011 ohadlevy@gmail.com - 0.3rc1-2
- rebuilt

* Thu May 05 2011 ohadlevy@gmail.com - 0.3rc1
- rebuilt

* Tue Mar 29 2011 ohadlevy@gmail.com - 0.2
- Version bump to 0.2

* Tue Mar 22 2011 ohadlevy@gmail.com - 0.2-rc1
- rebuilt

* Thu Feb 24 2011 ohadlevy@gmail.com - 0.1.7-rc5
- rebuilt

* Sat Feb 12 2011 ohadlevy@gmail.com - 0.1.7-rc4.1
- rebuilt

* Mon Jan 31 2011 ohadlevy@gmail.com - 0.1.7-rc3.1
- rebuilt

* Tue Jan 18 2011 ohadlevy@gmail.com - 0.1.7-rc2.1
- rebuilt

* Sat Jan 15 2011 ohadlevy@gmail.com - 0.1.7-rc2
- rebuilt

* Fri Dec 17 2010 ohadlevy@gmail.com - 0.1.7rc1
- rebuilt

* Mon Nov 29 2010 ohadlevy@gmail.com - 0.1.6-3
- rebuilt

* Fri Nov 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6-1
- Included fix for #461, as without it newly installed instances are not usable

* Thu Nov 11 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6
- New upstream version

* Sat Oct 30 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc2
- New release candidate
- Updated configuration file permssion not to break passenger

* Sun Sep 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc1
- Removed the depenecy upon rack 1.0.1 as its now bundled within Foreman

* Mon May 31 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.5-1
- New upstream version
- Added migration support between old directory layout to FHS compliancy, upgrades from 0.1-4.x should now work
- Added support for logrotate
- Cleanup old activescaffold plugin leftovers files

* Fri Apr 30 2010 Todd Zullinger <tmz@pobox.com> - 0.1.4-4
- Rework %%install for better FHS compliance
- Misc. adjustments to match Fedora/EPEL packaging guidelines
- Update License field to GPLv3+ to match README
- Use foreman as the primary group for the foreman user instead of puppet
- This breaks compatibility with previous RPM, as directories can't be replaced with links easily.

* Mon Apr 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1-4-3
- added status to startup script
- removed puppet module from the RPM

* Mon Apr 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-2
- Added startup script for built in webrick server
- Changed foreman user default shell to /sbin/nologin and is now part of the puppet group
- defaults to sqlite database

* Tue Apr 6 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-1
- Initial release.