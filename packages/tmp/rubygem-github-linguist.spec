# Generated from github-linguist-2.8.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name github-linguist

Name: rubygem-%{gem_name}
Version: 2.8.4
Release: 1%{?dist}
Summary: GitHub Language detection
Group: Development/Languages
License: 
URL: https://github.com/github/linguist
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(charlock_holmes) => 0.6.6
Requires: rubygem(charlock_holmes) < 0.7
Requires: rubygem(escape_utils) => 0.3.1
Requires: rubygem(escape_utils) < 0.4
Requires: rubygem(mime-types) => 1.19
Requires: rubygem(mime-types) < 2
Requires: rubygem(pygments.rb) => 0.4.2
Requires: rubygem(pygments.rb) < 0.5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description



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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/linguist
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.8.4-1
- Initial package
