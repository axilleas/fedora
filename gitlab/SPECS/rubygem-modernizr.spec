# Generated from modernizr-2.6.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name modernizr

Name: rubygem-%{gem_name}
Version: 2.6.2
Release: 1%{?dist}
Summary: Modernizr JS assets for Sprockets/Rails
Group: Development/Languages
License: MIT
URL: https://github.com/josh/ruby-modernizr
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(sprockets) => 2.0
Requires: rubygem(sprockets) < 3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Neatly packaged Modernizr JS assets for use in Sprockets or the Rails 3 asset pipeline.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.6.2-1
- Initial package
