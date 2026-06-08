import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import RecoveryCalculator from './views/RecoveryCalculator';
import CampaignPreview from './views/CampaignPreview';
import InactiveListAuditForm from './views/InactiveListAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'recovery-calculator': RecoveryCalculator,
  'campaign-preview': CampaignPreview,
  'inactive-list-audit-form': InactiveListAuditForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('recovery-calculator')} className={route === 'recovery-calculator' ? 'active' : ''}>RecoveryCalculator</button>
          <button onClick={() => setRoute('campaign-preview')} className={route === 'campaign-preview' ? 'active' : ''}>CampaignPreview</button>
          <button onClick={() => setRoute('inactive-list-audit-form')} className={route === 'inactive-list-audit-form' ? 'active' : ''}>InactiveListAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
