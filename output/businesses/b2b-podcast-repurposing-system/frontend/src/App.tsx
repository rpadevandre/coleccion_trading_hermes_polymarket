import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import BeforeAfterDemo from './views/BeforeAfterDemo';
import TranscriptUploadDemo from './views/TranscriptUploadDemo';
import ContentCalendarPreview from './views/ContentCalendarPreview';
import EpisodeAuditForm from './views/EpisodeAuditForm';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'before-after-demo': BeforeAfterDemo,
  'transcript-upload-demo': TranscriptUploadDemo,
  'content-calendar-preview': ContentCalendarPreview,
  'episode-audit-form': EpisodeAuditForm,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('before-after-demo')} className={route === 'before-after-demo' ? 'active' : ''}>BeforeAfterDemo</button>
          <button onClick={() => setRoute('transcript-upload-demo')} className={route === 'transcript-upload-demo' ? 'active' : ''}>TranscriptUploadDemo</button>
          <button onClick={() => setRoute('content-calendar-preview')} className={route === 'content-calendar-preview' ? 'active' : ''}>ContentCalendarPreview</button>
          <button onClick={() => setRoute('episode-audit-form')} className={route === 'episode-audit-form' ? 'active' : ''}>EpisodeAuditForm</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
