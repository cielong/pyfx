# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.3.0] - 2023-09-22
### Added
- Add a warning bar to show some interactive information, such as when pressing undefined key.

### Changed
- Switched to an Emacs-alike UI frame to always show the information bar.
- **Breaking** Renamed the configuration section name from *view* to *ui*.
- **Breaking** Removed *appearance* section and moved up *theme* section.

## [0.2.0] - 2022-10-26

### Added
- Add 200 ms timeout to all auto-complete query
- Support left mouse click to toggle expandable nodes

### Changed
- Keep JSON key order.  
  Previously, Pyfx internally sort the keys in alphabetical order to maintain 
  a sorted order of the keys. Thanks Python 3.7 change of dict, this is now not needed,
  because Python dict now maintains insertion order.

### Fixed
- Fix issue that unwanted logs shown in the UI when Pyfx is used as library
- Fix ANTLR inclusion in sdist and build warning @nullableVoidPtr

## [0.1.0] - 2022-08-28

### Added
- Add Flake8 coding style check.
- Improve description at help bar.
- Pop up a help page when pressing '?'

### Changed
- Pass data into Pyfx constructor instead of load it during after run.

### Fixed
- Fixed bounded method error by using ProcessPoolExecutor.
- Fixed resource file loading issue. 

## [0.1.0-beta.2] - 2021-07-29

### Added
- Support customize JSON node to render self-defined class.

### Changed
- Use Factory pattern to extract all the potential data sources.
- Lock dependency versions in setup.py file.

## [0.1.0-beta.1] - 2020-12-18

### Added
- Support for reading JSON from clipboard
- Support Palette (Theme) Configuration
- Reject mis-configuration at start up
- Expand all and collapse all key bindings for JSON browser
- Support second keyboard stroke configuration

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

[unreleased]: https://github.com/cielong/pyfx/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/cielong/pyfx/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/cielong/pyfx/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/cielong/pyfx/compare/v0.1.0-beta.2...v0.1.0
[0.1.0-beta.2]: https://github.com/cielong/pyfx/compare/v0.1.0-beta.1...v0.1.0-beta.2
[0.1.0-beta.1]: https://github.com/cielong/pyfx/compare/v0.1.0-beta...v0.1.0-beta.1
[0.1.0-beta]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.3...v0.1.0-beta
[0.1.0-alpha.3]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[0.1.0-alpha.2]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[0.1.0-alpha.1]: https://github.com/cielong/pyfx/compare/v0.1.0-alpha...v0.1.0-alpha.1
[0.1.0-alpha]: https://github.com/cielong/pyfx/v0.1.0-alpha
