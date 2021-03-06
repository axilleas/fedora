# Generated from jquery-ui-rails-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-ui-rails

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: jQuery UI packaged for the Rails asset pipeline
Group: Development/Languages
License: MIT and GPL
URL: https://github.com/joliss/jquery-ui-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(railties) >= 3.1.0
Requires: rubygem(jquery-rails) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
jQuery UI's JavaScript, CSS, and image files packaged for the Rails 3.1+ asset pipeline.

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

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/License.txt
%{gem_spec}
%{gem_instdir}/vendor
%{gem_instdir}/dependencies.js
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.2-1
- Initial package
