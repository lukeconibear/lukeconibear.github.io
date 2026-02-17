import type { CollectionEntry } from "astro:content";
import { normalizePath as sharedNormalizePath } from "../shared/normalize-path.mjs";

export type PageSection = "home" | "software" | "atmospheric_science";

export type SitePage = {
  slug: string;
  path: string;
  title: string;
  description?: string;
  summary?: string;
  section: PageSection;
  order: number;
};

export const siteMeta = {
  title: "Luke Conibear",
  description: "Software engineer focusing on machine learning and atmospheric science."
};

const sectionSortOrder: Record<PageSection, number> = {
  home: 0,
  software: 1,
  atmospheric_science: 2
};

export function normalizePath(pathname: string): string {
  return sharedNormalizePath(pathname);
}

export function pathFromSlug(slug: string): string {
  if (!slug || slug === "index") {
    return "/";
  }

  return normalizePath(`/${slug}`);
}

export function mapEntryToPage(entry: CollectionEntry<"pages">): SitePage {
  return {
    slug: entry.slug,
    path: pathFromSlug(entry.slug),
    title: entry.data.title,
    description: entry.data.description,
    summary: entry.data.summary,
    section: entry.data.section,
    order: entry.data.order ?? 0
  };
}

export function sortPages(pages: SitePage[]): SitePage[] {
  return [...pages].sort((left, right) => {
    const sectionDelta = sectionSortOrder[left.section] - sectionSortOrder[right.section];
    if (sectionDelta !== 0) {
      return sectionDelta;
    }

    const orderDelta = left.order - right.order;
    if (orderDelta !== 0) {
      return orderDelta;
    }

    return left.path.localeCompare(right.path);
  });
}
