# Generated from acts-as-taggable-on-2.4.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name acts-as-taggable-on

Name: rubygem-%{gem_name}
Version: 2.4.1
Release: 1%{?dist}
Summary: Advanced tagging for Rails
Group: Development/Languages
License: MIT
URL: https://github.com/mbleigh/acts-as-taggable-on
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(rails) >= 3
Requires: rubygem(rails) < 5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
With ActsAsTaggableOn, you can tag a single model on several contexts, such as
skills, interests, and awards. It also provides other advanced functionality.


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
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.4.1-1
- Initial package
