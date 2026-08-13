# Repository constraints

- Keep the published site as plain static HTML and CSS in `docs/`.
- Do not add JavaScript, package managers, dependencies, build tools,
  frameworks, plugins, remote assets, or custom deployment workflows.
- Do not add third-party GitHub Actions.
- Do not load scripts, fonts, styles, images, or embeds from remote origins.
- Preserve the restrictive Content Security Policy on every HTML page.
- Ask the owner before introducing any executable dependency or runtime.
- If an exception is approved, use only an exact stable release with no
  prerelease identifier, published at least seven full days earlier.
- Apply that exception policy to every package, library, dependency, runtime,
  tool, GitHub Action, and external asset.
- Never use version ranges, floating tags, moving branches, or unpinned
  GitHub Action references.
