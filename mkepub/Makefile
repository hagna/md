CC=gcc
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=testyaml.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=testyaml
INCLUDES=-I.
LIBYAML=yaml-0.1.4_patch/src/.libs/libyaml.a

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) $(LIBYAML) -o $@

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) $< -o $@
