#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RSclient
Version  : 0.7.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/RSclient_0.7-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RSclient_0.7-3.tar.gz
Summary  : Client for Rserve
Group    : Development/Tools
License  : GPL-2.0
Requires: R-RSclient-lib
BuildRequires : clr-R-helpers
BuildRequires : openssl-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-RSclient package.
Group: Libraries

%description lib
lib components for the R-RSclient package.


%prep
%setup -q -c -n RSclient

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521270526

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521270526
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSclient
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSclient
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSclient
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RSclient|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RSclient/DESCRIPTION
/usr/lib64/R/library/RSclient/INDEX
/usr/lib64/R/library/RSclient/LICENSE
/usr/lib64/R/library/RSclient/Meta/Rd.rds
/usr/lib64/R/library/RSclient/Meta/features.rds
/usr/lib64/R/library/RSclient/Meta/hsearch.rds
/usr/lib64/R/library/RSclient/Meta/links.rds
/usr/lib64/R/library/RSclient/Meta/nsInfo.rds
/usr/lib64/R/library/RSclient/Meta/package.rds
/usr/lib64/R/library/RSclient/NAMESPACE
/usr/lib64/R/library/RSclient/NEWS
/usr/lib64/R/library/RSclient/R/RSclient
/usr/lib64/R/library/RSclient/R/RSclient.rdb
/usr/lib64/R/library/RSclient/R/RSclient.rdx
/usr/lib64/R/library/RSclient/help/AnIndex
/usr/lib64/R/library/RSclient/help/RSclient.rdb
/usr/lib64/R/library/RSclient/help/RSclient.rdx
/usr/lib64/R/library/RSclient/help/aliases.rds
/usr/lib64/R/library/RSclient/help/paths.rds
/usr/lib64/R/library/RSclient/html/00Index.html
/usr/lib64/R/library/RSclient/html/R.css
/usr/lib64/R/library/RSclient/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RSclient/libs/RSclient.so
/usr/lib64/R/library/RSclient/libs/RSclient.so.avx2
/usr/lib64/R/library/RSclient/libs/RSclient.so.avx512