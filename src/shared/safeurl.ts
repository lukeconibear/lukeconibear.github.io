/**
 * Validates a URL to ensure it is safe to use in an 'href' or 'src' attribute.
 * Only allows 'http:', 'https:' protocols, relative paths, or protocol-relative URLs.
 * Blocks 'javascript:', 'data:', and other potentially dangerous schemes.
 * Returns the URL if safe, otherwise returns a safe default.
 * @param url The URL to validate
 * @param defaultValue The default value to return if the URL is unsafe (default: '#')
 * @returns A safe URL string
 */
export function getSafeUrl(url: string, defaultValue: string = "#"): string {
    if (!url) {
        return defaultValue;
    }

    const trimmedUrl = url.trim();

    // Allow protocol-relative URLs (e.g., //example.com)
    if (trimmedUrl.startsWith("//")) {
        return trimmedUrl;
    }

    // Allow absolute paths (e.g., /path/to/resource)
    if (trimmedUrl.startsWith("/")) {
        return trimmedUrl;
    }

    // Check for protocols
    try {
        // If it's a full URL, check the protocol
        const parsedUrl = new URL(trimmedUrl);
        const safeProtocols = ["http:", "https:"];
        if (safeProtocols.includes(parsedUrl.protocol)) {
            return trimmedUrl;
        }
        // If it has a protocol but it's not safe, return default
        return defaultValue;
    } catch (e) {
        // If URL constructor fails, it's either a relative path or an invalid URL.

        // Check if it looks like it has a protocol (e.g., "javascript:...", "data:...", "mailto:...")
        // A protocol starts with a letter and is followed by letters, digits, '+', '.', or '-'
        if (/^[a-z][a-z0-9+.-]*:/i.test(trimmedUrl)) {
            // It has a protocol, but since URL() failed, it might be malformed or a scheme 
            // not handled by the URL constructor in this environment.
            // To be safe, if it has any protocol other than what we've already allowed, we block it.
            return defaultValue;
        }

        // If it doesn't have a protocol, it's a relative path (e.g., "notebooks/plot.html", "plot.html")
        // These are generally safe as they will be resolved relative to the current page.
        return trimmedUrl;
    }
}
