OUT ?= aoc
PKG := github.com/jimmynguyen/advent-of-code/cli
PKG_LIST := $(shell go list ${PKG}/... | grep -v /vendor/)
GO_FILES := $(shell find . -name '*.go' | grep -v /vendor/)

all: clean vet lint test build

build:
	@go build -v -o ${HOME}/go/bin/${OUT} ${PKG}

test:
	@go test -short ${PKG_LIST}

vet:
	@go vet ${PKG_LIST}

lint:
	@staticcheck ${PKG_LIST}

run: build
	./${OUT}

clean:
	-@rm ${HOME}/go/bin/${OUT}

.PHONY: vet lint test build run