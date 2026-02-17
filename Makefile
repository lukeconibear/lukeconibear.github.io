NOTEBOOK_NAMES := plot_emulator plot_india_solid_fuel

.PHONY: install clean build dev check update-packages refresh-notebooks security-check

install:
	npm ci

clean:
	rm -rf dist .astro

build:
	npm run build

dev:
	npm run dev

check:
	npm run check

update-packages:
	npm update

refresh-notebooks:
	@for notebook in $(NOTEBOOK_NAMES); do \
		jupyter nbconvert --to html docs/atmospheric_science/$${notebook}.ipynb --TemplateExporter.exclude_input=True --output $${notebook}.html --output-dir public/notebooks; \
	done

security-check:
	npm run audit
