import re
from collections import Counter

LOG_FILE = "access_errors.log"

CODE_MEANINGS = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not found",
    405: "Method not allowed",
    408: "Request Timeout",
    409: "Conflict",
    429: "Too Many requests",
    500: "Internal server error",
    502: "Bad gateway",
    503: "Service unavailable",
    504: "Gateway timeout"
}

STATUS_CODE_PATTERN = re.compile(r"\b([4-5]\d{2})\b")

def parse_log(filepath):
    """Count occurances of each 4xx/5xx status code in the log file."""
    counter = Counter()
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = STATUS_CODE_PATTERN.search(line)
            if match:
                code = int(match.group(1))
                counter[code] += 1
    return counter

def print_summary_table(counter):
    print(f"{'code':<6}{'Count':<8}{'Meaning'}")
    print("-" * 70)
    for code, count in counter.most_common():
        meaning = CODE_MEANINGS.get(code, "Unknown status code")
        print(f"{code:<6}{count:<8}{meaning}")

def most_frequent_cause(counter):
    if not counter:
        print("No error codes found in log.")
        return
    top_code, top_count = counter.most_common(1)[0]
    meaning = CODE_MEANINGS.get(top_code, "Unknown status code")
    print(f"\nMost frequent error: {top_code} ({top_count} occurrences)")
    print(f"Meaning: {meaning}")
    print("Likely cause: " + likely_cause_text(top_code))


def likely_cause_text(code):
    causes = {
        404: "Broken links, outdated bookmarks, or misconfigured routes are sending traffic to urls that no longer exist",
        500: "Unhandled exception in application code, or a bad deploy is crashing requests before a response can be formed.",
        403: "Permission checks or auth middleware are rejecting requests possibly due to expired tokens or overly strict access rules",
        502: "Backend service crashing restarting or returning malformed responses that the proxy can't relay",
        503: "server likely overloaded or intentionally down for maintanence/deployment"
    }
    return causes.get(code, "Investigate server/application logs around")

if __name__ == "__main__":
    counts = parse_log(LOG_FILE)
    print_summary_table(counts)
    most_frequent_cause(counts)