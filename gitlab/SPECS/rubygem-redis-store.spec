# Generated from redis-store-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-store

Name: rubygem-%{gem_name}
Version: 1.1.3
Release: 1%{?dist}
Summary: Redis stores for Ruby frameworks
Group: Development/Languages
License: MIT
URL: https://github.com/jodosha/redis-store/tree/master/redis-store
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(redis) >= 2.2.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Namespaced Rack::Session, Rack::Cache, I18n and cache Redis stores for Ruby
web frameworks.


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

%check
pushd .%{gem_instdir}
#testrb2 -Ilib test/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.3-1
- Initial package
