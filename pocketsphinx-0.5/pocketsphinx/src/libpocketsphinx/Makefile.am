ARCH   = `uname -m | sed s/i.86/i386/`_`uname -s | tr A-Z a-z`

lib_LTLIBRARIES = libpocketsphinx.la

libpocketsphinx_la_LDFLAGS = -version-info 1:0:0

libpocketsphinx_la_SOURCES =			\
	acmod.c					\
	bin_mdef.c				\
	blkarray_list.c				\
	dict.c					\
	fsg_history.c				\
	fsg_lextree.c				\
	fsg_search.c				\
	hmm.c					\
	kdtree.c				\
	mdef.c					\
	ms_gauden.c				\
	ms_mgau.c				\
	ms_senone.c				\
	ngram_search.c				\
	ngram_search_fwdtree.c			\
	ngram_search_fwdflat.c			\
	ps_lattice.c				\
	s2_semi_mgau.c				\
	tmat.c					\
	vector.c				\
	pocketsphinx.c

noinst_HEADERS =				\
	pocketsphinx_internal.h			\
	acmod.h					\
	ngram_search.h				\
	bin_mdef.h				\
	blkarray_list.h				\
	dict.h					\
	fsg_history.h				\
	fsg_lextree.h				\
	fsg_search_internal.h			\
	hmm.h					\
	kdtree.h				\
	mdef.h					\
	ms_gauden.h				\
	ms_mgau.h				\
	ms_senone.h				\
	ngram_search.h				\
	ngram_search_fwdtree.h			\
	ngram_search_fwdflat.h			\
	ps_lattice_internal.h			\
	posixwin32.h				\
	s2_semi_mgau.h				\
	tmat.h					\
	vector.h

INCLUDES = -I$(top_srcdir)/include \
           -I$(top_builddir)/include 
