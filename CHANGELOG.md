# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Support for reading JSON from clipboard
- Support Palette (Theme) Configuration
- Reject mis-configuration at start up

### Changed
- Replace autocomplete with ANTLR4 based autocomplete
- Distinguish different json type with different palette
- Use Mediator pattern to restructure UI module

### Fixed
- Focus line jumping when toggle on closed braces

## [0.1.0-beta] - 2020-11-15

### Added

- Support Key Mapping configuration
- Add modes "emacs" and "vim" as predefined key mappings

### Fixed

- Focus line jumping around when moving up / below

## [0.1.0-alpha.3] - 2020-10-18

### Added

- Support for reading JSON from pipe

## [0.1.0-alpha.2] - 2020-10-17

### Added

- Auto-completion support for pyfx
- Add log configuration

## [0.1.0-alpha.1] - 2020-10-12

### Added

- Add doctest into the CI
- Add Travis CI test for MacOS
- Host docs on readTheDocs

## [0.1.0-alpha] - 2020-10-11

### Added

- Initial commit with pyfx

[unreleased]: https://github.com/cielong/pyfx/compare/v0.1.0-beta...HEAD
[0.1.0-beta]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.3...v0.1.0-beta
[0.1.0-alpha.3]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[0.1.0-alpha.2]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[0.1.0-alpha.1]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha...v0.1.0-alpha.1
[0.1.0-alpha]: https://github.com/cielong/pyfx/v0.1.0-alpha
