"""Rattish initialized file ;; meaning_space=default """

#import rattish.libs_resolve as LIBS
import os

# RATTISH PROJECT - https://github.com/rattish 

def default___space(core, string):
	"""Rattish command ;; default , SPACE """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	 
	#	DOCS=	0x20.md 
	#	ASCII=	32
	#	NAME=	SPACE
	#	FUNCTION=	default___space

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x20.md 

def default___exclamation_mark(core, string):
	"""Rattish command ;; default , EXCLAMATION MARK """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	!
	#	DOCS=	0x21.md 
	#	ASCII=	33
	#	NAME=	EXCLAMATION MARK
	#	FUNCTION=	default___exclamation_mark

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x21.md 

def default___quotation_mark(core, string):
	"""Rattish command ;; default , QUOTATION MARK """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	"
	#	DOCS=	0x22.md 
	#	ASCII=	34
	#	NAME=	QUOTATION MARK
	#	FUNCTION=	default___quotation_mark

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x22.md 

def default___number_sign(core, string):
	"""Rattish command ;; default , NUMBER SIGN """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	#
	#	DOCS=	0x23.md 
	#	ASCII=	35
	#	NAME=	NUMBER SIGN
	#	FUNCTION=	default___number_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x23.md 

def default___dollar_sign(core, string):
	"""Rattish command ;; default , DOLLAR SIGN """
	if string.strip():
		core.context = string.strip()
	else:
		core.memory["LAST_CONTEXT"] = core.context
		core.context = "LAST_CONTEXT"

	#	CHAR=	$
	#	DOCS=	0x24.md 
	#	ASCII=	36
	#	NAME=	DOLLAR SIGN
	#	FUNCTION=	default___dollar_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x24.md 

def default___percent_sign(core, string):
	"""Rattish command ;; default , PERCENT SIGN """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	%
	#	DOCS=	0x25.md 
	#	ASCII=	37
	#	NAME=	PERCENT SIGN
	#	FUNCTION=	default___percent_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x25.md 

def default___ampersand(core, string):
	"""Rattish command ;; default , AMPERSAND """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	&
	#	DOCS=	0x26.md 
	#	ASCII=	38
	#	NAME=	AMPERSAND
	#	FUNCTION=	default___ampersand

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x26.md 

def default___apostrophe(core, string):
	"""Rattish command ;; default , APOSTROPHE """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	'
	#	DOCS=	0x27.md 
	#	ASCII=	39
	#	NAME=	APOSTROPHE
	#	FUNCTION=	default___apostrophe

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x27.md 

def default___left_parenthesis(core, string):
	"""Rattish command ;; default , LEFT PARENTHESIS """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	(
	#	DOCS=	0x28.md 
	#	ASCII=	40
	#	NAME=	LEFT PARENTHESIS
	#	FUNCTION=	default___left_parenthesis

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x28.md 

def default___right_parenthesis(core, string):
	"""Rattish command ;; default , RIGHT PARENTHESIS """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	)
	#	DOCS=	0x29.md 
	#	ASCII=	41
	#	NAME=	RIGHT PARENTHESIS
	#	FUNCTION=	default___right_parenthesis

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x29.md 

def default___asterisk(core, string):
	"""Rattish command ;; default , ASTERISK """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	*
	#	DOCS=	0x2a.md 
	#	ASCII=	42
	#	NAME=	ASTERISK
	#	FUNCTION=	default___asterisk

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2a.md 

def default___plus_sign(core, string):
	"""Rattish command ;; default , PLUS SIGN """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	+
	#	DOCS=	0x2b.md 
	#	ASCII=	43
	#	NAME=	PLUS SIGN
	#	FUNCTION=	default___plus_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2b.md 

def default___comma(core, string):
	"""Rattish command ;; default , COMMA """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	,
	#	DOCS=	0x2c.md 
	#	ASCII=	44
	#	NAME=	COMMA
	#	FUNCTION=	default___comma

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2c.md 

def default___hyphenminus(core, string):
	"""Rattish command ;; default , HYPHEN-MINUS """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	-
	#	DOCS=	0x2d.md 
	#	ASCII=	45
	#	NAME=	HYPHEN-MINUS
	#	FUNCTION=	default___hyphenminus

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2d.md 

def default___full_stop(core, string):
	"""Rattish command ;; default , FULL STOP """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	.
	#	DOCS=	0x2e.md 
	#	ASCII=	46
	#	NAME=	FULL STOP
	#	FUNCTION=	default___full_stop

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2e.md 

def default___solidus(core, string):
	"""Rattish command ;; default , SOLIDUS """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	/
	#	DOCS=	0x2f.md 
	#	ASCII=	47
	#	NAME=	SOLIDUS
	#	FUNCTION=	default___solidus

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x2f.md 

def default___colon(core, string):
	"""Rattish command ;; default , COLON """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	:
	#	DOCS=	0x3a.md 
	#	ASCII=	58
	#	NAME=	COLON
	#	FUNCTION=	default___colon

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3a.md 

def default___semicolon(core, string):
	"""Rattish command ;; default , SEMICOLON """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	;
	#	DOCS=	0x3b.md 
	#	ASCII=	59
	#	NAME=	SEMICOLON
	#	FUNCTION=	default___semicolon

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3b.md 

def default___lessthan_sign(core, string):
	"""Rattish command ;; default , LESS-THAN SIGN """
	if string.strip():
		core.memory[core.context] = input(string)
	else:
		core.memory[core.context] = input(core.memory[core.context])

	#	CHAR=	<
	#	DOCS=	0x3c.md 
	#	ASCII=	60
	#	NAME=	LESS-THAN SIGN
	#	FUNCTION=	default___lessthan_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3c.md 

def default___equals_sign(core, string):
	"""Rattish command ;; default , EQUALS SIGN """
	if string.strip():
		core.memory[core.context] = string
	else:
		del core.memory[core.context]

	#	CHAR=	=
	#	DOCS=	0x3d.md 
	#	ASCII=	61
	#	NAME=	EQUALS SIGN
	#	FUNCTION=	default___equals_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3d.md 

def default___greaterthan_sign(core, string):
	"""Rattish command ;; default , OUTPUT """
	if string.strip():
		print(string.strip())
	else:
		print(core.memory[core.context])

	#	CHAR=	>
	#	DOCS=	0x3e.md 
	#	ASCII=	62
	#	NAME=	GREATER-THAN SIGN
	#	FUNCTION=	default___greaterthan_sign

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3e.md 

def default___question_mark(core, string):
	"""Rattish command ;; default , QUESTION MARK """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	?
	#	DOCS=	0x3f.md 
	#	ASCII=	63
	#	NAME=	QUESTION MARK
	#	FUNCTION=	default___question_mark

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x3f.md 

def default___commercial_at(core, string):
	"""Rattish command ;; default , COMMERCIAL AT """
	to_be_imported = ""
	if string.strip():
		to_be_imported = string.strip()
	else:
		to_be_imported = core.memory[core.context]
	if os.path.exists(to_be_imported):
		with open(to_be_imported) as f:
			core + f.read()

	#	CHAR=	@
	#	DOCS=	0x40.md 
	#	ASCII=	64
	#	NAME=	COMMERCIAL AT
	#	FUNCTION=	default___commercial_at

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x40.md 

def default___left_square_bracket(core, string):
	"""Rattish command ;; default , LEFT SQUARE BRACKET """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	[
	#	DOCS=	0x5b.md 
	#	ASCII=	91
	#	NAME=	LEFT SQUARE BRACKET
	#	FUNCTION=	default___left_square_bracket

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x5b.md 

def default___reverse_solidus(core, string):
	"""Rattish command ;; default , REVERSE SOLIDUS """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	\
	#	DOCS=	0x5c.md 
	#	ASCII=	92
	#	NAME=	REVERSE SOLIDUS
	#	FUNCTION=	default___reverse_solidus

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x5c.md 

def default___right_square_bracket(core, string):
	"""Rattish command ;; default , RIGHT SQUARE BRACKET """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	]
	#	DOCS=	0x5d.md 
	#	ASCII=	93
	#	NAME=	RIGHT SQUARE BRACKET
	#	FUNCTION=	default___right_square_bracket

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x5d.md 

def default___circumflex_accent(core, string):
	"""Rattish command ;; default , CIRCUMFLEX ACCENT """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	^
	#	DOCS=	0x5e.md 
	#	ASCII=	94
	#	NAME=	CIRCUMFLEX ACCENT
	#	FUNCTION=	default___circumflex_accent

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x5e.md 

def default___low_line(core, string):
	"""Rattish command ;; default , LOW LINE """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	_
	#	DOCS=	0x5f.md 
	#	ASCII=	95
	#	NAME=	LOW LINE
	#	FUNCTION=	default___low_line

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x5f.md 

def default___grave_accent(core, string):
	"""Rattish command ;; default , GRAVE ACCENT """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	`
	#	DOCS=	0x60.md 
	#	ASCII=	96
	#	NAME=	GRAVE ACCENT
	#	FUNCTION=	default___grave_accent

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x60.md 

def default___left_curly_bracket(core, string):
	"""Rattish command ;; default , LEFT CURLY BRACKET """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	{
	#	DOCS=	0x7b.md 
	#	ASCII=	123
	#	NAME=	LEFT CURLY BRACKET
	#	FUNCTION=	default___left_curly_bracket

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x7b.md 

def default___vertical_line(core, string):
	"""Rattish command ;; default , VERTICAL LINE """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	|
	#	DOCS=	0x7c.md 
	#	ASCII=	124
	#	NAME=	VERTICAL LINE
	#	FUNCTION=	default___vertical_line

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x7c.md 

def default___right_curly_bracket(core, string):
	"""Rattish command ;; default , RIGHT CURLY BRACKET """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	}
	#	DOCS=	0x7d.md 
	#	ASCII=	125
	#	NAME=	RIGHT CURLY BRACKET
	#	FUNCTION=	default___right_curly_bracket

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x7d.md 

def default___tilde(core, string):
	"""Rattish command ;; default , TILDE """
	if string.strip():
		pass #core.blank()
	else:
		pass #core.blank()

	#	CHAR=	~
	#	DOCS=	0x7e.md 
	#	ASCII=	126
	#	NAME=	TILDE
	#	FUNCTION=	default___tilde

# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/0x7e.md 


def main(core):

	core[" "] = default___space
	core["!"] = default___exclamation_mark
	core["\""] = default___quotation_mark
	core["#"] = default___number_sign
	core["$"] = default___dollar_sign
	core["%"] = default___percent_sign
	core["&"] = default___ampersand
	core["'"] = default___apostrophe
	core["("] = default___left_parenthesis
	core[")"] = default___right_parenthesis
	core["*"] = default___asterisk
	core["+"] = default___plus_sign
	core[","] = default___comma
	core["-"] = default___hyphenminus
	core["."] = default___full_stop
	core["/"] = default___solidus
	core[":"] = default___colon
	core[";"] = default___semicolon
	core["<"] = default___lessthan_sign
	core["="] = default___equals_sign
	core[">"] = default___greaterthan_sign
	core["?"] = default___question_mark
	core["@"] = default___commercial_at
	core["["] = default___left_square_bracket
	core["\\"] = default___reverse_solidus
	core["]"] = default___right_square_bracket
	core["^"] = default___circumflex_accent
	core["_"] = default___low_line
	core["`"] = default___grave_accent
	core["{"] = default___left_curly_bracket
	core["|"] = default___vertical_line
	core["}"] = default___right_curly_bracket
	core["~"] = default___tilde

	# RATTISH PROJECT - https://rattish.github.io/ 

