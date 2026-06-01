# Production automation workflows through third-party integration chains

Matt's tooling approach extends beyond code generation into production deployment through carefully orchestrated third-party service chains. Rather than building monolithic deployment solutions, he composes existing tools into reliable automation pipelines that move content from development to publication.

## The Dropbox→Zapier→Buffer pattern

`course-video-manager` demonstrates sophisticated production workflow automation through a three-service chain for social media posting. The workflow coordinates file synchronization, webhook triggers, and content scheduling:

1. **Local staging** — copy video files into a Dropbox folder monitored for sync completion
2. **Sync polling** — use `dropbox filestatus` to wait for cloud synchronization before proceeding  
3. **Webhook trigger** — send structured payload (caption + file path) to Zapier webhook
4. **File discovery** — Zapier finds the synced file in Dropbox by path and retrieves its share URL
5. **Content scheduling** — Buffer receives the file URL and caption, adding it to the publication queue

This chain separates concerns: Dropbox handles file distribution, Zapier provides the integration glue, and Buffer manages publication scheduling. The app coordinates the flow but delegates each specialized function to the appropriate service.

## Fail-safe design through monitoring and coordination

The workflow includes explicit coordination mechanisms to handle the distributed nature of the pipeline. File sync status polling prevents race conditions between local copy and webhook trigger. Environment variables (`BUFFER_POSTS_PATH`, `ZAPIER_BUFFER_WEBHOOK_URL`) make the integration points configurable without hardcoding service details into the application logic.

This approach trades direct control for reliability — rather than implementing file hosting, webhook infrastructure, and social media APIs directly, the application orchestrates proven third-party services and handles only the coordination logic that's specific to the domain.

## Sources

- `sources/mattpocock/course-video-manager/README.md.md` — origin: https://github.com/mattpocock/course-video-manager/blob/0dabcefa76514471cea6d99ab494d065f3bb5c71/README.md